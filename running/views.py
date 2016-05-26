import time
from django.shortcuts import render

# Create your views here.
from run.http import JsonResponse, JsonError
from run.test_data import *
import json
from auth_token.decorators import token_cache_required
from run.models import *
from django.contrib.auth.models import User




# @token_cache_required
from run.utils import change_time_from_str_to_datatime


def upload_result(request):
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
    value={
        "running_result_distance":run["distance"],
        "running_result_duration":time.strftime('%H:%M:%S', time.gmtime(float(run["duration"]))),
        "running_result_starttime":starttime,
        "running_result_endtime":endtime,
    }
    # print starttime,endtime
    try:
        re = RunningResult(**value)
        re.user = user
        re.save()
    except Exception,e:
        print e.message
        return JsonError("running result create fail")
    else:
        return JsonResponse({})



