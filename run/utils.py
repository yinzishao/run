#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'yinzishao'
import time

def change_time_from_str_to_datatime(str):
    gt =time.gmtime(int(str))
    return time.strftime("%Y-%m-%d %H:%M:%S",gt)

# print time.strftime('%H:%M:%S', time.gmtime(61.23))
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