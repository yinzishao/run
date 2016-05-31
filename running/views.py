#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import datetime
from django.shortcuts import render

# Create your views here.
from run.http import JsonResponse, JsonError
from run.test_data import *
import json
from auth_token.decorators import token_cache_required
from run.models import *
from django.contrib.auth.models import User
from run.utils import change_time_from_str_to_datatime
from django.db import transaction
from django.db.models import Sum,Count


#上传一次跑步结果并且返回前三
@token_cache_required
def upload_result(request):
    # with open("")
    # return JsonResponse(RUNNING_RESULT)
    try:
        # r_r =RUNNING_RESULT_2
        r_r = json.loads(request.body)
    except Exception,e:
        return JsonError("json format error")


    try:
        userpk = r_r["id"]
        user = AuthUser.objects.get(id=userpk)

        run = r_r["run"]
        locations = run["locations"]
        # print locations

        # locations_sorted = sorted(locations, lambda x, y: float(x["time"]) - float(y["time"]))
        locations_sorted = sorted(locations, lambda x, y: int(float(x["time"])) - int(float(y["time"])))

        #时间戳有小数点！！
        starttime = change_time_from_str_to_datatime(locations_sorted[0]["time"])
        endtime = change_time_from_str_to_datatime(locations_sorted[-1]["time"])
        #跑步结果对象
        run_res_value={
            "running_result_distance":run["distance"],
            "running_result_duration":time.strftime('%H:%M:%S', time.gmtime(float(run["duration"]))),
            "running_result_starttime":starttime,
            "running_result_endtime":endtime,
        }

    except Exception,e:
        # print e.message
        return JsonError("json parameter is not valid")


    #创建事务
    try:

        with transaction.atomic():
            re = RunningResult(**run_res_value)
            re.user = user
            re.save()
            # print "re success"

            # re = RunningResult.objects.get(running_result_id=4)
            #根据run对象创建其所有locations
            for ls in locations_sorted:
                # print ls
                #每个location对象
                loc_value={
                    "latitude":ls["latitude"],
                    "longitude":ls["longitude"],
                    "time":change_time_from_str_to_datatime(ls["time"]),
                    # "time":213
                }

                loc_obj =Locations(**loc_value)
                loc_obj.running_result = re
                loc_obj.save()
            # print "loc success"
    except Exception,e:
        # print e.message
        return JsonError("upload fail")
    else:
        #返回排名和前三名
        return return_first_three(re)



"""
需要考虑当中间某个不能上传成功的时候应该怎么办。
解决办法：返回错误的id？
"""
@token_cache_required
def upload_mul_result(request):
    try:
        mul_res=json.loads(request.body)
        # mul_res=RUNNING_MUL_RESULT
        result=[]
        for i in mul_res["run"]:
            one_res = {}
            one_res["id"] = mul_res["id"]
            one_res["run"] = i
            ret = upload_one_result(one_res)
            content =ret.content
            ret_dic = json.loads(content)
            if ret_dic["success"]=="0":
                return ret
            else:
                result.append(ret_dic['running_result_id'])
            # if isinstance(ret,JsonError):
            #     pass
        return JsonResponse({"running_result_id":result})
    except Exception,e:
        return JsonError(e.message)

    # a = JsonResponse()
    # ret_dic =json.loads(a.content)
    # print content,type(content)
    # if ret_dic["success"]=="1":
    #         return JsonError("ss")
    # return a

#上传一个running_result,成功则返回一个包含id的字典
def upload_one_result(running_result):
    running_result_id =0
    r_r =running_result

    try:
        userpk = r_r["id"]
        user = AuthUser.objects.get(id=userpk)


        run = r_r["run"]

        locations = run["locations"]
        # print locations

        locations_sorted = sorted(locations, lambda x, y: int(x["time"]) - int(y["time"]))


        starttime = change_time_from_str_to_datatime(locations_sorted[0]["time"])
        endtime = change_time_from_str_to_datatime(locations_sorted[-1]["time"])
        #跑步结果对象
        run_res_value={
            "running_result_distance":run["distance"],
            "running_result_duration":time.strftime('%H:%M:%S', time.gmtime(float(run["duration"]))),
            "running_result_starttime":starttime,
            "running_result_endtime":endtime,
        }


    except Exception:
        return JsonError("user is not valid")
    #创建事务
    try:

        with transaction.atomic():
            re = RunningResult(**run_res_value)
            re.user = user
            re.save()
            # print "re success"
            running_result_id=re.running_result_id
            # re = RunningResult.objects.get(running_result_id=4)
            #根据run对象创建其所有locations
            for ls in locations_sorted:
                # print ls
                #每个location对象
                loc_value={
                    "latitude":ls["latitude"],
                    "longitude":ls["longitude"],
                    "time":change_time_from_str_to_datatime(ls["time"]),
                    # "time":213
                }

                loc_obj =Locations(**loc_value)
                loc_obj.running_result = re
                loc_obj.save()
            # print "loc success"
    except Exception,e:
        # print e.message
        return JsonError("upload fail")
    else:
        return JsonResponse({"running_result_id":str(running_result_id)})

#返回本次排名和前三名
def return_first_three(my_rs):
    # RunningResult.objects.all()
    #返回距离前三名
    #将mysql里面的distance（varchar）转换为小数
    try:
        rs_sort =RunningResult.objects.all()\
        .extra({'running_result_distance_de':"CAST(running_result_distance as DECIMAL)"})\
        .order_by('-running_result_distance_de')
        rs_fir_thr = rs_sort[:3]

        # my_rs = RunningResult.objects.get(running_result_id=9)
        result={}
        run = []
        #个人排名
        my_ranking =  list(rs_sort.values_list('running_result_id', flat=True)).index(my_rs.running_result_id)+1
        result["my_ranking"]=str(my_ranking)
        result["running_result_id"]=my_rs.running_result_id
        #返回前三
        for i in  rs_fir_thr:
            data={}
            data['username'] = i.user.username
            data['distance'] = i.running_result_distance
            run.append(data)
        result["three"]=run



        # print type(rs_sort)
        # print rs_sort.index(my_rs)
        # print rs_sort[2] ==my_rs
        # for index, item in enumerate(rs_sort):
        #     # print index,type(item)
        #     print my_rs.running_result_id,item.running_result_id
        #     if item.running_result_id == my_rs.running_result_id:
        #         print index
        #         break
        #     print "end"

        # print rs_sort.index(my_rs)
        return JsonResponse(result)
    except Exception,e:
        # print e.message
        return JsonError("get the first three fail")
#根据跑步结果id返回当天排名：
@token_cache_required
def get_ranking(request):
    try:
        # data=RANK
        data = json.loads(request.body)
        r_r_id=data["running_result_id"]
        r_r = RunningResult.objects.get(running_result_id=r_r_id)
        r_r_start = str(r_r.running_result_starttime)
        # r_r_start
        day = time.strptime(r_r_start, '%Y-%m-%d %H:%M:%S').tm_mday
        month = time.strptime(r_r_start, '%Y-%m-%d %H:%M:%S').tm_mon
        year = time.strptime(r_r_start, '%Y-%m-%d %H:%M:%S').tm_year
        # print r_r_start,day,month,year

        rs_sort =RunningResult.objects.filter(running_result_starttime__year=year)\
            .filter(running_result_starttime__month=month)\
            .filter(running_result_starttime__day=day)\
            .extra({'running_result_distance_de':"CAST(running_result_distance as DECIMAL)"})\
            .order_by('-running_result_distance_de')
        result = {}
        #个人排名
        my_ranking =  list(rs_sort.values_list('running_result_id', flat=True)).index(r_r.running_result_id)+1
        result["my_ranking"]=str(my_ranking)
        #根据需求返回列表
        page = int(data["page"])
        interval = int(data["interval"])
        start =(page-1)*interval
        rs_list = rs_sort[start:start+interval]
        print rs_sort,rs_list
        rank=[]
        for i in rs_list:
            evr= {}
            rs_user = i.user
            evr["username"]=rs_user.username
            evr["distance"]=i.running_result_distance
            rank.append(evr)
        result["ranking"]=rank
        return JsonResponse(result)
    except Exception,e:
        return JsonError(e.message)
#返回某个月的所有跑步结果
@token_cache_required
def get_month_res(request):
    # data = MONTH_REQUEST
    try:
        data = json.loads(request.body)
        id =data["id"]
        month = data["month"]
        user = AuthUser.objects.get(id=1)
        # print user.username
        year,month=data["month"].split("-")[0],data["month"].split("-")[1]
        rs = user.runningresult_set.filter(running_result_starttime__year=year,running_result_starttime__month=month)

        # from django.core import serializers
        # data =serializers.serialize("json",rs)
        # print data
        # print "````````````````````````"
        # print rs[0].toJSON()
        result=[]
        # print rs
        if rs != None:
            for every_res in rs:
                #每个跑步结果的坐标集
                res={}
                res["distance"]=every_res.running_result_distance

                sp = every_res.running_result_duration

                # print str(every_res.running_result_duration)
                # sp = time.strptime(str(every_res.running_result_duration),'%H:%M:%S')
                # res["duration"]=str(sp.tm_sec+sp.tm_min*60+sp.tm_hour*3600)
                res["duration"]=str(sp.second+sp.minute*60+sp.hour*3600)
                res["starttime"]=str(every_res.running_result_starttime)
                res["endtime"]=str(every_res.running_result_endtime)
                res["running_result_id"]=str(every_res.running_result_id)
                # print res["duration"]
                res["locations"]=[]
                loc_set = every_res.locations_set.all()
                # from django.core import serializers
                # data =serializers.serialize("json",loc_set)
                # print data
                for every_loc in loc_set:
                    el={}
                    el["latitude"]=every_loc.latitude
                    el["longitude"]=every_loc.longitude
                    # el["time"]=time.mktime(time.strptime(every_loc.time, '%Y-%m-%d %H:%M:%S'))
                    el["time"]=str(int(time.mktime(every_loc.time.timetuple())))
                    # print el["time"]
                    res["locations"].append(el)
                result.append(res)


        return JsonResponse({"run":result})
    except Exception,e:
        return JsonError(e.message)


#返回一个月的总排名
@token_cache_required
def get_month_ranking(request):
    try:
        # data = MONTH_RANK
        data = json.loads(request.body)
        # year,month =data["time"].split("-")
        # rs_sort =RunningResult.objects.filter(running_result_starttime__year=year)\
        #         .filter(running_result_starttime__month=month)\
        #         .extra({'running_result_distance_de':"CAST(running_result_distance as DECIMAL)"})\
        #         .order_by('-running_result_distance_de')\
        #         .values('user_id').annotate(ds=Count("user_id"))
        # print rs_sort
        year_month = data["time"]
        res = my_custom_sql(year_month)
        # print res
        result={}
        for index,values in enumerate(res):
            if values["user_id"] == int(data["id"]):
                result["my_ranking"]=str(index+1)
                print index,type(values["user_id"])
        page =int(data["page"])
        interval=int(data["interval"])
        strat = (page-1)*interval
        r =res[strat:strat+5]
        for i in r:
            sum = str(i.pop("amount_sum"))
            id = i.pop("user_id")
            user = AuthUser.objects.get(id=id)
            i["username"]=user.username
            i["sum"]=sum
        result["ranking"]=r
        return JsonResponse(result)
    except Exception,e:
        return JsonError(e.message)

from django.db import connection
#用原始sql查询
def my_custom_sql(year_month):
    cursor = connection.cursor()
    # year_month ="2016-05"
    # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    cur ="select user_id,sum(running_result_distance) as amount_sum from running_result where strcmp(date_format(running_result_starttime,'%Y-%m'),'"+year_month+"') =0 group by user_id order by amount_sum desc;"
    cursor.execute(cur)
    # row = cursor.fetchall()

    return dictfetchall(cursor)

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

#需考虑传过来的时间和服务器的时间的误差
def walk_test(request):
    try:
        walk = WALK
        user = AuthUser.objects.get(id=walk["id"])
        time_tmp = datetime.datetime.now()
        walk_set = walk["walk"]
        for i in walk_set:
            oneDayAgo = (time_tmp - datetime.timedelta(days = 1))
            otherStyleTime = oneDayAgo.strftime("%Y-%m-%d")
            time_tmp =oneDayAgo
            walk_obj = Walk(time=otherStyleTime,value=i)
            walk_obj.user =user
            walk_obj.save()
    except Exception,e:
        return JsonError("fail")
    else:
        return JsonResponse()


def get_test(request):
    walk =WALK
    id = walk["id"]
    year = walk["time"].split("-")[0]
    month = walk["time"].split("-")[1]
    user = AuthUser.objects.get(id=id)
    walk_set = user.walk_set.filter(time__year=year).filter(time__month=month).order_by('time')
    for i in walk_set:
        pass