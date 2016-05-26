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
        "distance": "1000.22",
        "duration": "10.22",
        "locations": [
            {
                "longitude": "100",
                "latitude": "100",
                "time": "1464272180"
            },
            {
                "longitude": "200",
                "latitude": "200",
                "time": "1464272190"
            },
            {
                "longitude": "300",
                "latitude": "300",
                "time": "1464272200"
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