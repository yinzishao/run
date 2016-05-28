#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

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
                "longitude": "100.2",
                "latitude": "100.2",
                "time": "1464273280"
            },
            {
                "longitude": "200.3",
                "latitude": "200.3",
                "time": "1464273290"
            },
            {
                "longitude": "300.5",
                "latitude": "300.5",
                "time": "1464273310"
            }
        ]
    }
}

RUNNING_MUL_RESULT = {
    "id": "1",
    "token": "ss",
    "run": [
        {
        "distance": "222.22",
        "duration": "30.22",
        "locations": [
            {
                "longitude": "100.2",
                "latitude": "100.2",
                "time": "1464273280"
            },
            {
                "longitude": "200.3",
                "latitude": "200.3",
                "time": "1464273290"
            },
            {
                "longitude": "300.5",
                "latitude": "300.5",
                "time": "1464273310"
            }
        ]
        },
        {
        "distance": "222.22",
        "duration": "30.22",
        "locations": [
            {
                "longitude": "100.2",
                "latitude": "100.2",
                "time": "1464273280"
            },
            {
                "longitude": "200.3",
                "latitude": "200.3",
                "time": "1464273290"
            },
            {
                "longitude": "300.5",
                "latitude": "300.5",
                "time": "1464273310"
            }
        ]
        }
    ]
}
# RUNNING_MUL_RESULT.append(RUNNING_RESULT)
# RUNNING_MUL_RESULT.append(RUNNING_RESULT)
# RUNNING_MUL_RESULT.append(RUNNING_RESULT)


USER_INF={
    "token":"1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id":"1",
    "user_avatar":"头像",
    "user_height":"170",
    "user_weight":"55",
    "user_sex":"男",
    "user_birth":"1995-10-18"
}

MONTH_REQUEST={
    "token":"1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id":"1",
    "month":"2016-5"

}