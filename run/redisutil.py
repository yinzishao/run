#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'yinzishao'

from redis import Redis
host = 'localhost'
port=6379
r = Redis(host,port,db=0)

#(token,userid)插入redis
def insert_token(data):
    # data={"token": "zASR0MqjgvD_t6bWl9H8x9SPIR1", "userid": "FgsrjCxMETo6hgMNoeR8Tufa1-o"}
    token = data['token']
    userpk =data['userpk']
    r.set(token,userpk)
    # userid_fromredis = r.get(token)
    # print userid_fromredis

#根据token返回userpk
def get_userpk(token):
    # print token,type(token)
    return r.get(token)

#定时清理set（过期时间）
def clear_token():
    pass
# r.flushdb()

#1成功
def delete_token(token):
    return r.delete(token)

token = u"1b46US:_uw-1cM6p3M8H10r7SF3DR6EQCk"
# print get_userpk(token)
# print delete_token("1b45lx:L6pYuXNvwVY3nfo14AkvYsJv-Hk")
# sty = "17:"+"FgsrjCxMETo6hgMNoeR8Tufa1-o"
# print "17:FgsrjCxMETo6hgMNoeR8Tufa1-o"  ==sty