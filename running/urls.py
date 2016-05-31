#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'yinzishao'

from django.conf.urls import url

urlpatterns = [
    url(r'^upload_result/?$',"running.views.upload_result",name="upload_result"),
    url(r'^get_month_res/?$',"running.views.get_month_res",name="get_month_res"),
    url(r'^upload_mul_result/?$',"running.views.upload_mul_result",name="upload_mul_result"),
    url(r'^walk_test/?$',"running.views.walk_test",name="walk_test"),
    url(r'^get_ranking/?$',"running.views.get_ranking",name="get_ranking"),
    url(r'^get_month_ranking/?$',"running.views.get_month_ranking",name="get_month_ranking"),
]