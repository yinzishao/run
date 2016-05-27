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
# @token_cache_required
def upload_result(request):
    """
    # return JsonResponse(RUNNING_RESULT)
    r_r =RUNNING_RESULT
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
        """
    return return_first_three()
        #返回排名和前三名




def return_first_three():
    # RunningResult.objects.all()
    #返回距离前三名
    #将mysql里面的distance（varchar）转换为小数
    try:
        rs_sort =RunningResult.objects.all()\
        .extra({'running_result_distance_de':"CAST(running_result_distance as DECIMAL)"})\
        .order_by('-running_result_distance_de')
        rs_fir_thr = rs_sort[:3]

        my_rs = RunningResult.objects.get(running_result_id=9)

        result = []
        my_ranking =  list(rs_sort.values_list('running_result_id', flat=True)).index(my_rs.running_result_id)+1
        result.append({"my_ranking":my_ranking})
        for i in  rs_fir_thr:
            data={}
            data['username'] = i.user.username
            data['distance'] = i.running_result_distance
            result.append(data)



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