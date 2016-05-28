#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'yinzishao'

"""
测试api 的虚拟数据
"""

RUNNING_RESULT = {
    "id": "1",
    "token": "ss",
    "run": {
        "distance": "222.22",
        "duration": "30.22",
        "locations": [
            {
                "longitude": "100",
                "latitude": "100",
                "time": "1464273280"
            },
            {
                "longitude": "200",
                "latitude": "200",
                "time": "1464273290"
            },
            {
                "longitude": "300",
                "latitude": "300",
                "time": "1464273310"
            }
        ]
    }
}

# print locations

#
# print RUNNING_RESULT
# import json
# r_r_j = json.dumps(RUNNING_RESULT)
# print r_r_j
# print "----------------------"
# r_r_s = json.loads(r_r_j)
# print r_r_s
# print [i["time"] for i in  r_r_j["run"]["locations"]]
#
# print RUNNING_RESULT