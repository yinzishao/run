# -*- coding:utf-8 -*-
import json

from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from run.redisutil import insert_token
from tokens import make_token_in_cache
from decorators import token_cache_required
from run.http import JsonResponse, JsonError
# from django.utils import simplejson

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
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        realname = request.POST.get('realname',None)

        if not (username and password and realname):
            print request.body
            try:
                request_data= json.loads(request.body,"utf-8")
                # request_data= simplejson.loads(request.body)
                username =  request_data["username"]
                password =  request_data["password"]
                realname =  request_data["realname"]
            except Exception,e:
                print e
                return JsonError(e.message+"is required")
            # email =request_data['email']
        print username,password,realname
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
                if user.is_active:
                    return HttpResponse("success")
                else:

                    return JsonError("fail")
            else:
                return JsonError("User already exists")
        else:
            return JsonError("username , password or realname is none")


            # print request_data
            # return HttpResponse(request.body,content_type="application/json")
            # print request_data
        # print username,password
        # data['username']=username
        # data['password']=password
        # return HttpResponse(json.dumps(data),content_type="application/json")

    return JsonError("post is required")


#用户密码登录返回token
def login_from_pwd(request):
    username=None
    password=None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    # username="yzs"
    # password="pwd"
        if not (username and password):
                # print request.body
                request_data= json.loads(request.body)
                username =  request_data["username"]
                password =  request_data["password"]
                print username,password
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
                data = {
                    'token':token,
                    'userpk':str(user.pk),
                }
                return JsonResponse(data)
            else:
                return JsonError("Fail")
        else:
            return JsonError("username and password is required")
    else:
            return JsonError("POST is required")







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

@token_cache_required
def change_inf(request):
    return JsonError("developing")





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