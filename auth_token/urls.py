#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url

__author__ = 'yinzishao'


urlpatterns = [
    url(r'^login/?$','auth_token.views.loginview',name='loginview'),
    url(r'^signup/?$','auth_token.views.signup',name='signup'),
    url(r'^auth/?$','auth_token.views.auth',name='auth'),
    url(r'^test/?$','auth_token.views.test',name='test'),
    url(r'^login_from_pwd/?$','auth_token.views.login_from_pwd',name='login_from_pwd'),
    url(r'^change_inf/?$','auth_token.views.change_inf',name='change_inf'),
    url(r'^upload_ava/?$','auth_token.views.upload_ava',name='upload_ava'),
    url(r'^change_pwd/?$','auth_token.views.change_pwd',name='change_pwd'),
    # url(r'^token/new.json$', token_new, name='api_token_new'),
    # url(r'^token/(?P<token>.{24})/(?P<user>\d+).json$', token, name='api_token'),
]
