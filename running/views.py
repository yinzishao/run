from django.shortcuts import render

# Create your views here.
from run.http import JsonResponse, JsonError
from run.test_data import *
import json
from auth_token.decorators import token_cache_required
@token_cache_required

def upload_result(request):

    # running_result =
    running_result_json = json.loads(RUNNING_RESULT)
    return JsonResponse(RUNNING_RESULT)
