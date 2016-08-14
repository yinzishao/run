# -*- coding:utf-8 -*-
import json

from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from run.models import UserInformation, AuthUser
from run.redisutil import insert_token
from run.test_data import *
from run.utils import save_pic
from tokens import make_token_in_cache
from decorators import token_cache_required
from run.http import JsonResponse, JsonError
# from django.utils import simplejson
domain = "http://119.29.115.117:8080"
defalut_avatar ="/static/auth_token/avatar/1.png"
# @token_required
def loginview(request):
    # c = {"yin":"yin"}
    # c.update(csrf(request))
    basic_auth = request.META.get('HTTP_AUTHORIZATION')
    # print basic_auth
    return render(request,'login.html')
    # return render_to_response('login.html', c,)

# def auth(request):
#     result =  token_new(request)
#     return result

#注册
def signup(request):
    data={}
    # print request.method
    try:
        if request.method == "POST":
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            realname = request.POST.get('realname',None)

            if not (username and password and realname):
                # print request.body
                try:
                    request_data= json.loads(request.body,"utf-8")
                    # request_data= simplejson.loads(request.body)
                    username =  request_data["username"]
                    password =  request_data["password"]
                    realname =  request_data["realname"]
                except Exception,e:
                    # print e
                    return JsonError(e.message+"is required")
                # email =request_data['email']
            # print username,password,realname
            if username and password and realname:
                try:
                    # print "test get user"
                    user = User.objects.get(username=username)
                    # print user
                except User.DoesNotExist,e:
                    # print repr(realname)
                    user = User.objects.create_user(username,password=password,first_name=realname[:-2],last_name=realname[-2:])
                    # user = User.objects.create_user(username,password=password,first_name=realname.encode('unicode_escape'))
                    # user = User.objects.create_user(username,password=password,first_name=u"尹子勺")

                    if user and user.is_active:
                        login(request,user)
                        token = make_token_in_cache(user).split(":",1)[1]

                        #将{token:id}放在redis内
                        redis_data = {
                            'token':token,
                            'userpk':user.pk,
                        }
                        insert_token(redis_data)
                        #将pk加密

                        # userpk_encode = user_signer.sign(user.pk).split(":",1)[1]
                        # data = {
                        #     'token':token,
                        #     'userpk':userpk_encode,
                        # }
                        data = {
                            'token':token,
                            'id':str(user.pk),
                            'username':username,
                            'realname':realname,
                            'avatar':domain+defalut_avatar,
                            'height':"165",
                            'weight':"55",
                            'sex':"男",
                            'birth':"1990-01-01",
                        }
                        user =AuthUser.objects.get(id=user.pk)
                        inf = user.userinformation_set.all()
                        if len(inf)!= 0:
                            inf = inf[0]
                            data["avatar"]=domain+inf.user_avatar
                            data["height"]=inf.user_height
                            data["weight"]=inf.user_weight
                            data["sex"]=inf.user_sex
                            data["birth"]=str(inf.user_birth)
                        return JsonResponse(data)
                    else:

                        return JsonError("用户被关进小黑屋")
                else:
                    return JsonError("用户已经存在")
            else:
                return JsonError("用户名、密码和姓名不能为空")


                # print request_data
                # return HttpResponse(request.body,content_type="application/json")
                # print request_data
            # print username,password
            # data['username']=username
            # data['password']=password
            # return HttpResponse(json.dumps(data),content_type="application/json")

        return JsonError("请POST请求")
    except Exception,e:
        return JsonError(e.message)


#用户密码登录返回token
def login_from_pwd(request):
    try:
        username=None
        password=None
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        # username="yzs"fhttp://127.0.0.1/
        # password="pwd"
            if not (username and password):
                    # print request.body
                    request_data= json.loads(request.body)
                    username =  request_data["username"]
                    password =  request_data["password"]
                    # print username,password
            if username and password:
                user = authenticate(username=username,password=password)

                if user and user.is_active:
                    login(request,user)
                    token = make_token_in_cache(user).split(":",1)[1]

                    #将{token:id}放在redis内
                    redis_data = {
                        'token':token,
                        'userpk':user.pk,
                    }
                    insert_token(redis_data)
                    #将pk加密

                    # userpk_encode = user_signer.sign(user.pk).split(":",1)[1]
                    # data = {
                    #     'token':token,
                    #     'userpk':userpk_encode,
                    # }
                    #不加密
                    username = user.username
                    realname = user.first_name+user.last_name

                    data = {
                        'token':token,
                        'id':str(user.pk),
                        'username':username,
                        'realname':realname,
                        'avatar':domain+defalut_avatar,
                        'height':"165",
                        'weight':"55",
                        'sex':"男",
                        'birth':"1990-01-01",
                    }
                    user =AuthUser.objects.get(id=user.pk)
                    inf = user.userinformation_set.all()
                    if len(inf)!= 0:
                        inf = inf[0]
                        if inf.user_avatar !=None:
                            data["avatar"]=domain+inf.user_avatar
                        if inf.user_weight !=None:
                            data["weight"]=inf.user_weight
                        if inf.user_sex !=None:
                            data["sex"]=inf.user_sex
                        if inf.user_birth !=None:
                            data["birth"]=str(inf.user_birth)
                        if inf.user_height !=None:
                            data["height"]=inf.user_height

                    # print data
                    return JsonResponse(data)
                else:
                    return JsonError("Fail")
            else:
                return JsonError("username and password is required")
        else:
                return JsonError("POST is required")
    except Exception,e:
        return JsonError(e.message)







@token_cache_required
# @csrf_exempt
def test(request):
    # basic_auth = request.META.get('HTTP_AUTHORIZATION')
    # userpk = request.POST.get('userpk', request.GET.get('userpk'))
    # token = request.POST.get('token', request.GET.get('token'))
    # print userpk,token
    # if not (userpk and token) and basic_auth:
    #         auth_method, auth_string = basic_auth.split(' ', 1)
    #
    #         if auth_method.lower() == 'basic':
    #             auth_string = b64decode(auth_string.strip())
    #             userpk, token = auth_string.decode().split(':', 1)
    # if not (userpk and token):
    #     # print request.body
    #     request_data= json.loads(request.body)
    #     userpk = request_data['userpk']
    #     token = request_data['token']
    # print userpk,token
    # us = None
    # pw = None
    # print request.method
    # if request.method == 'POST':
    #     print "POST"
    #     # print request.META
    #     print request.POST
    #     us = request.POST.get('userpk')
    #     pw = request.POST.get('token')
    # print us,pw


    return JsonResponse({})

    # data={
    #     "token": "1b46US:_uw-1cM6p3M8H10r7SF3DR6EQCk",
    #     "userpk": "FgsrjCxMETo6hgMNoeR8Tufa1-o",
    # }
    # return check_token_in_cache(data)

    #
    # """
    # 测试密码登陆
    # """
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    # username="yzs"
    # password="pwd"
    # if username and password:
    #     user = authenticate(username=username,password=password)
    #
    #     if user and user.is_active:
    #         login(request,user)
    #         token = make_token_in_cache(user).split(":",1)[1]
    #
    #         #将{token:id}放在redis内
    #         redis_data = {
    #             'token':token,
    #             'userpk':user.pk,
    #         }
    #         insert_token(redis_data)
    #         #将pk加密
    #         userpk = user_signer.sign(user.pk).split(":",1)[1]
    #
    #         data = {
    #             'token':token,
    #             'userpk':userpk,
    #         }
    #         return HttpResponse(json.dumps(data),content_type="application/json")
    #     else:
    #         return HttpResponse("Fail")


def createUser(**kwargs):
    username = kwargs['username']
    password = kwargs['password']
    email = kwargs['email']
    try:
        user = User.objects.create_user(username,email,password)
    except IntegrityError:
        JsonError("Fail")
    # if user.

#修改个人信息
@token_cache_required
def change_inf(request):
    try:
        # data = USER_INF
        data = json.loads(request.body)
        # avatar = getattr(data,"user_avatar",None)
        user_id = data["id"]
        try:
            user = AuthUser.objects.get(id=user_id)
        except AuthUser.DoesNotExist,e:
            return JsonError("id is not valid")
        #修改真实名字
        realname = data["realname"]
        # print realname
        user.first_name=realname[:-2]
        user.last_name=realname[-2:]
        user.save()
        del data["id"]
        del data["token"]
        del data["realname"]
        # avatar =data["user_avatar"]
        #上传图片返回连接
        # print len(avatar)

        domain = "http://polls.nat123.net"
        # data["user_avatar"]=pic_url
        try:
            user_inf_set=user.userinformation_set.all()
            if len(user_inf_set) ==0:
                user_inf = UserInformation(**data)
                user_inf.user =user
                user_inf.save()
            else:
                user_inf_set.update(**data)
                user_inf = user_inf_set[0]
                # user_inf.user_avatar = getattr(data,"user_avatar",None)
                # user_inf.user_height = getattr(data,"user_height",None)
                # user_inf.user_weight = getattr(data,"user_weight",None)
                # user_inf.user_sex = getattr(data,"user_sex",None)
        except Exception,e:
            # print e.message
            return JsonError("inf Fail")


        result={}
        if user_inf.user_avatar=="":
            res_avatar = defalut_avatar
        else:
            res_avatar = user_inf.user_avatar
        result["avatar"]=domain+res_avatar
        result["height"]=user_inf.user_height
        result["weight"]=user_inf.user_weight
        result["sex"]=user_inf.user_sex
        result["birth"]=str(user_inf.user_birth)
        result["realname"]=user.first_name+user.last_name
        return JsonResponse(result)
        # avatar = getattr(data,"user_avatar",None)
    except Exception,e:
        # print e.message
        return JsonError("Fail")

#上传头像
@token_cache_required
def upload_ava(request):
    try:
        # data =UPLOAD_PIC_2
        data = json.loads(request.body)
        avatar = data["avatar"]
        id = data["id"]
        user =AuthUser.objects.get(id=id)
        try:
            pic_url = save_pic(avatar[1:-1].replace(" ",""),id)
        except Exception,e:
            return JsonError("save pic fail")
        try:
            user_inf_set=user.userinformation_set.all()
            if len(user_inf_set) ==0:
                value ={
                'height':"165",
                'weight':"55",
                'sex':"男",
                'birth':"1990-01-01"
                }
                user_inf = UserInformation(user_avatar=pic_url)
                user_inf.user =user
                user_inf.save()
            else:
                user_inf = user_inf_set[0]
            result={}
            result["avatar"]=domain+user_inf.user_avatar
            return JsonResponse(result)

        except Exception,e:
            # print e.message
            return JsonError("inf Fail")



    except Exception,e:
        return JsonError("data should be json")

#修改密码
@token_cache_required
def change_pwd(request):
    try:
        # data=PWD
        data=json.loads(request.body)
        id=data["id"]
        a_user = AuthUser.objects.get(id=id)
        username = a_user.username
        password=data["old_password"]
        new_password=data["new_password"]

        if username and password:
                user = authenticate(username=username,password=password)

                if user and user.is_active:
                    user.set_password(new_password)
                    user.save()
                    return JsonResponse()
                else:
                    return JsonError("password is not valid")
        else:
            return JsonError("Fail")

    except Exception,e:
        return JsonError(e.message)

#
#
# def auth_and_login(request, onsuccess='/secure', onfail='/login/'):
#     user = authenticate(username=request.POST['email'], password=request.POST['password'])
#     if user is not None and user.is_active:
#         login(request, user)
#         request.session['name'] = "yin"
#         return redirect(onsuccess)
#     else:
#         return redirect(onfail)
#
# def create_user(username, email, password):
#     user = User(username=username, email=email)
#     user.set_password(password)
#     user.save()
#     return user
#
# def user_exists(username):
#     user_count = User.objects.filter(username=username).count()
#     if user_count == 0:
#         return False
#     return True
#
# def sign_up_in(request):
#     post = request.POST
#     if not user_exists(post['email']):
#         user = create_user(username=post['email'], email=post['email'], password=post['password'])
#         return auth_and_login(request)
#     else:
#         return redirect("/login/")
