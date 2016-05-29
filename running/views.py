#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
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



#上传一次跑步结果并且返回前三
@token_cache_required
def upload_result(request):

    # return JsonResponse(RUNNING_RESULT)
    # r_r =RUNNING_RESULT
    r_r = json.loads(request.body)
    userpk = r_r["id"]
    try:
        user = AuthUser.objects.get(id=userpk)
    except Exception:
        return JsonError("user is not valid")

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
        print e.message
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
    mul_res=RUNNING_MUL_RESULT
    for i in mul_res["run"]:
        one_res = {}
        one_res["id"] = mul_res["id"]
        one_res["run"] = i
        ret = upload_one_result(one_res)
        content =ret.content
        ret_dic = json.loads(content)
        if ret_dic["success"]=="0":
            return ret

        # if isinstance(ret,JsonError):
        #     pass
    return JsonResponse()

    # a = JsonResponse()
    # ret_dic =json.loads(a.content)
    # print content,type(content)
    # if ret_dic["success"]=="1":
    #         return JsonError("ss")
    # return a

#上传一个running_result
@token_cache_required
def upload_one_result(running_result):
    r_r =running_result
    # r_r = json.loads(request.body)
    userpk = r_r["id"]
    try:
        user = AuthUser.objects.get(id=userpk)
    except Exception:
        return JsonError("user is not valid")

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
        print e.message
        return JsonError("upload fail")
    else:
        return JsonResponse()

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
        print e.message
        return JsonError("get the first three fail")

#返回某个月的所有跑步结果
@token_cache_required
def get_month_res(requset):
    # data = MONTH_REQUEST
    data = json.loads(requset.body)
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

