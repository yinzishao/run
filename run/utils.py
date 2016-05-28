#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'yinzishao'
import time

def change_time_from_str_to_datatime(str):
    gt =time.gmtime(int(str))
    return time.strftime("%Y-%m-%d %H:%M:%S",gt)

# sp = time.strptime("00:01:30",'%H:%M:%S')
# print sp.tm_sec

# print int(time.mktime(time.strptime('2016-05-26 14:16:30', '%Y-%m-%d %H:%M:%S')))



#
# print time.strftime('%H:%M:%S', time.gmtime(1464440120))
# print float("10.22")
# print time.time()
# gt =time.gmtime(1464271512)
# print time.strftime("%Y-%m-%d %H:%M:%S",gt)
#
# now = time.time()
# gt =time.gmtime(now)
# strft = time.strftime("%Y-%m-%d %H:%M:%S",gt)
# print now,gt,strft
# name = u"尹子勺"
# print repr(name)