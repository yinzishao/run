#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'yinzishao'

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from tokens import check_token_in_cache_encode,check_token_in_cache

class TokenCacheBackend(ModelBackend):
    def authenticate(self,pk,token):
        data={}
        data["token"]=token
        data["userpk"]=pk
        # print data
        # user,inf=check_token_in_cache_encode(data)
        user,inf=check_token_in_cache(data)
        print user
        if user:
            return user
        else:
            return None

