#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from run.http import JsonError

__author__ = 'yinzishao'
from base64 import b64decode

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from functools import wraps

def token_cache_required(view_func):
    @csrf_exempt
    @wraps(view_func)
    def _wrapped_view(request,*args,**kwargs):
        userpk = None
        token = None
        basic_auth = request.META.get('HTTP_AUTHORIZATION')
        userpk = request.POST.get('id', request.GET.get('id'))
        # userpk = request.POST.get('userpk')
        token = request.POST.get('token', request.GET.get('token'))
        # token = request.POST.get('token')
        print userpk,token
        if not (userpk and token) and request.body:
        # print request.body
            try:
                request_data= json.loads(request.body)
            except Exception:
                return JsonError("data should be json")
            else:
                userpk = request_data['id']
                token = request_data['token']
        if not (userpk and token) and basic_auth:
            auth_method, auth_string = basic_auth.split(' ', 1)

            if auth_method.lower() == 'basic':
                auth_string = b64decode(auth_string.strip())
                userpk, token = auth_string.decode().split(':', 1)
        if not (userpk and token):
            return JsonError("Must include 'id' and 'token' parameters with request.")
        # print userpk,token
        user = authenticate(pk=userpk, token=token)
        # print user
        if user:
            request.user = user
            return view_func(request, *args, **kwargs)
        return JsonError("authentication failer ")
    return _wrapped_view