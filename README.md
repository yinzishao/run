# Running-Life---iOS

是基于HealthKit和高德地图开发的健康跑步助手。记录跑步路线和距离，并能与他人比较跑步排名。  

##ios演示地址和源码：https://github.com/caixindong/Running-Life---iOS

##本人负责的是**后台部分**：  
  使用Python的Django框架进行后台开发,提供API给ios客户端。
  客户端并不能使用cookie，所以为了适应手机用户的调用后台API，开发了一个基于token的认证应用。  
  利用时间戳等信息加密生成token用作令牌，装饰后台API，实现安全访问和状态维持。  
  并用**redis**将token做内存缓存，加快访问速度。 
  具体代码实现在auth_token应用里面。

##TODO：refer_token、权限控制等。

##使用方法很简单：
  只需在view里面的方法中用@token_cache_required装饰就可以了。
  




#说明文档：

host: http://119.29.115.117:8080/  
POST  
Content-Type:application/json  



出现错误返回的信息格式：
```
{
    "success": "0",
    "error": "error message"
}
```


#根据页数和间隔返回一个月的排名列表和自己的排名
POST  
/get_month_ranking/  
```
{
    "token": "1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id": "1",
    "time": "2016-05",
    "page": "1",	#第一页
    "interval": "5"	#每次取5个
}
```

Return
```
{
    "ranking": [		#第一名
        {
            "sum": "11556.64",	#该月跑的总距离
            "username": "yinzishao"	#用户名
        },
        {			#第二名
            "sum": "572.856647491",
            "username": "458770054"
        }
    ],
    "my_ranking": "1",
    "success": "1"
}
```
#根据页数和间隔返回某周的排名列表和自己的排名    
POST    
/get_week_ranking/   
```
{
    "token": "1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id": "1",
    "time": "2016年05月第1周",
    "page": "1",	#第一页
    "interval": "5"	#每次取5个
}
```
Return
```
{
    "ranking": [
        {
            "username": "yinzishao",
            "distance": "3000.22",
“avatar”:”url”,
“calorie”:””
        },
        {
            "username": "yinzishao",
            "distance": "2222.22"
        },
        {
            "username": "yinzishao",
            "distance": "2000.22"
        },
        {
            "username": "yinzishao",
            "distance": "1000.22"
        },
        {
            "username": "yinzishao",
            "distance": "1000.22"
        }
    ],
    "my_ranking": "7",
    "success": "1"
}
```

#根据跑步结果id返回该次跑步当天排名：
/get_ranking/
POST
```
{
    "token":"1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id":"1",
    "running_result_id":"12",
    "page":"1",
    "interval":"5"
}
```
Return
```
{
    "ranking": [
        {
            "username": "yinzishao",
            "distance": "3000.22",
“avatar”:”url”,
“calorie”:””
        },
        {
            "username": "yinzishao",
            "distance": "2222.22"
        },
        {
            "username": "yinzishao",
            "distance": "2000.22"
        },
        {
            "username": "yinzishao",
            "distance": "1000.22"
        },
        {
            "username": "yinzishao",
            "distance": "1000.22"
        }
    ],
    "my_ranking": "7",
    "success": "1"
}
```
#上传多个结果
/upload_mul_result/
POST
```
{
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
```
改为：
```
{
    "running_result_id": [
        "35",
        "36"
    ],
    "success": "1"
}
```
#上传跑步结果
/upload_result/
POST
```
{
    "id": "1",
    "token": "1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "run": {
        "distance": "24.27618026733398",
        "duration": "4",
        "locations": [
            {
                "longitude": "37.32888846",
                "latitude": "122.02686653",
                "time": "1464522773.159730"
            },
            {
                "longitude": "200",
                "latitude": "200",
                "time": "200"
            },
            {
                "longitude": "300",
                "latitude": "300",
                "time": "300"
            }
        ]
    }
}
```
return 自己排名和前三排名加了结果id
```
{
"my_ranking": "8",
"running_result_id": 37,
    "three": [
        {
            "username": "yinzishao",
            "distance": "4000.22"
        },
        {
            "username": "yinzishao",
            "distance": "3000.22"
        },
        {
            "username": "yinzishao",
            "distance": "2222.22"
        }
    ],
    "success": "1"
}
```


失败：
```
#用户id错误
{
    "success": "0",
    "error": "user is not valid"
}
```

```
{
    "success": "0",
    "error": "upload fail"
}
```


#上传图片借口
POST
/upload_ava/
```
{
    "token": "1b6gYD:8P3oqpq5RYVwlfh9epdTUvp3lwU",
    "id": "16",
    "avatar": "ssssssssssssssssssssssssssssssssssssssss"
}
```
Return
```
{
    "avatar": "http://polls.nat123.net/static/auth_token/avatar/16.png",
    "success": "1"
}
```
#修改密码
/change_pwd/
```
{
    "token": "1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id": "1",
    "old_password": "yinzishao",
    "new_password": "yinzishao"
}
```
Return

成功:
```
{
    "success": "1"
}
```
错误:
```
{
    "success": "0",
    "error": "password is not valid"
}
```
#注册,已修改。现在是用户名和密码注册，添加姓名
/signup/
POST
```
{
    "username": "yinzishao",
"password": "yinzishao",
"realname":"尹子勺"
}
```
return 

#注册成功
```
{
    "username": "caixxx",
    "token": "1b6gnv:M6klTdiDfJAt0NKkOLwDp_10DiQ",
    "id": "17",
    "realname": "蔡兴东",
    "success": "1",
    "avatar": "http://polls.nat123.net/static/auth_token/avatar/1.png",
    "height": "165",
    "weight": "55",
    "sex": "男",
    "birth": "1990-01-01"
}
```
#登陆,返回token和id
/login_from_pwd/

POST
```
{
    "username": "yinzishao",
    "password": "yinzishao"
}
```
Return
#默认

```
{
    "username": "cai",
    "token": "1b6sGv:jZIHe72S7alJDQQeTntNZ1b5B44",
    "id": "15",
    "realname": "蔡兴东",
    "weight": "55",
    "height": "165",
    "sex": "男",
    "success": "1",
    "birth": "1990-01-01",
    "avatar": "默认"
}
```

#测试token和id是否登陆成功
/test/

POST
```
{
    "token": "1b46US:_uw-1cM6p3M8H10r7SF3DR6EQCk",
    "id": "1"
}
```
return

成功：
```
{
    "scccess": "1"
}
```
失败：
```
{
    "success": "0",
    "error": "authentication failer"
}

#
{
    "success": "0",
    "error": "data should be json"
}

#
{
    "success": "0",
    "error": "Must include 'id' and 'token' parameters with request."
}

#token超过有效时间，请重新登陆
{
    "success": "0",
    "error": "expired please login again"
}
#id出错
{
    "success": "0",
    "error": "id is not valid"
}
```
#修改个人资料(头像还是字符串类型，需更改)
/change_inf/
POST
```
{
    "token": "1b6sLO:Ssaf6Y5sEYFmgCu3LoFUI3lVtZQ",
    "id": "15",
    "user_height": "170",
    "user_weight": "55",
    "user_sex": "男",
"user_birth": "1995-10-18",
"realname":"中心及"
}
```

注意上传数据的字段和返回的数据不一样
成功（修改信息成功后返回修改的信息）：
```
{
    "realname": "中心纪",
    "weight": "55",
    "success": "1",
    "sex": "男",
    "avatar": "http://polls.nat123.net/static/auth_token/avatar/16.png",
    "birth": "1995-10-18",
    "height": "170"
}
```
失败：
```
{
    "success": "0",
    "error": "Fail"
}
```


#返回某个月的所有跑步结果
/get_month_res/	
POST
```
{
    "token":"1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id":"1",
    "month":"2016-5"

}
```
Return:

```	
{
    "run": [
        {
            "distance": "3000.22",
            "running_result_id": "4",
            "locations": [
                {
                    "latitude": "100",
                    "longitude": "100",
                    "time": "1464243380"
                },
                {
                    "latitude": "200",
                    "longitude": "200",
                    "time": "1464243390"
                },
                {
                    "latitude": "300",
                    "longitude": "300",
                    "time": "1464243400"
                }
            ],
            "starttime": "2016-05-26 14:16:20",
            "duration": "10",
            "endtime": "2016-05-26 14:16:40"
        },
        {
            "distance": "1000.22",
            "running_result_id": "8",
            "locations": [
                {
                    "latitude": "100",
                    "longitude": "100",
                    "time": "1464244380"
                },
                {
                    "latitude": "200",
                    "longitude": "200",
                    "time": "1464244390"
                },
                {
                    "latitude": "300",
                    "longitude": "300",
                    "time": "1464244400"
                }
            ],
            "starttime": "2016-05-26 14:33:00",
            "duration": "20",
            "endtime": "2016-05-26 14:33:20"
        }
    ],
    "success": "1"
}
```
如果无则是：
```
{
    "run": [],
    "success": "1"
}
```

