from django.shortcuts import render,HttpResponse
from tool.message import Message
from tool.random_add import product_code
from redis import Redis
from cmfz.settings import API_KEY
from tool.repath import is_phone
import re
from login.models import Permission,Role,User
from login.init_permission.init_permmission import init_permission

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

# 连接redis
rds=Redis(host='127.0.0.1',port=6379)


def page(request):
    return render(request,'login.html')


@csrf_exempt
def get_code(request):
    mobile=request.POST.get('mobile')

    # 这里验证号码格式
    result=is_phone(mobile)
    # 手机号码格式正确发送验证码
    if result:
        # 生成随机码
        code = product_code()

        get_redis_moile = rds.get(mobile)

        if get_redis_moile:
            return HttpResponse('no')
        else:


            # 发送验证码
            message=Message(API_KEY)
            message.send_message(mobile,code)
            rds.set(mobile, code, 10)  # 确保用户发送频率
            rds.set(mobile + '_2', code, 20)  # 确保验证码存活周期
            return HttpResponse('ok')
    #     格式不正确直接pass
    else:
        return HttpResponse('middle')


@csrf_exempt
def verify_code(request):
    # 获取用户输入的code
    code=request.POST.get('code')
    # 获取用户输入的电话号码
    mobile = request.POST.get('mobile')
    # 通过redis查询该号码的验证码进行判断
    get_redis_code=rds.get(mobile+'_2')
    redis_code=get_redis_code.decode()
    if code==redis_code:

        if User.objects.filter(phone=str(mobile)):
            print('准备跳转页面')
            user=User.objects.filter(phone=mobile).first()
            init_permission(user,request)
            return HttpResponse('ok')

    return HttpResponse('no')