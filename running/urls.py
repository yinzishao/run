#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'yinzishao'

from django.conf.urls import url

urlpatterns = [
    url(r'^upload_result/?$',"running.views.upload_result",name="upload_result")
]