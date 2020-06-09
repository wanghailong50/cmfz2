from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from userapp.models import User
import json
# Create your views here.


def get_all_data(request):

    users=User.objects.all().order_by('id')

    num = request.GET.get('rows')  # 每页数量
    page = request.GET.get('page')  # 当前页码
    # 进行分页
    all_page = Paginator(users, num)
    # 获取每一页对象
    student_page = all_page.page(page).object_list
    data = {
        "page": page,  # 页码
        "total": all_page.num_pages,  # 总页数
        "records": all_page.count,  # 总条数
        "rows": list(student_page)  # 分页后的每一页的对象
    }

    def mydefalut(u):
        if isinstance(u, User):
            return {'id': u.id, 'phone': u.phone.name, 'username': str(u.username), 'danger': str(u.danger),
                    'pic': str(u.picture),'address':u.address.name,'sign':u.sign,'status':u.wait.name}

    result = json.dumps(data, default=mydefalut)

    return HttpResponse(result)


@csrf_exempt
def ban_user(request):
    id=request.POST.get('id')
    ban=request.POST.get('ban')
    print(id,ban)
    if ban=='0':
        ban='未封禁'
    else:
        ban='已封禁'
    result=User.objects.filter(id=id)[0]
    print(result)
    print(result.wait,ban)
    result.wait=ban
    result.save()
    return HttpResponse('success')



# 获取折线图数据
@cache_page(timeout=100,key_prefix='cacheRedis')
def get_data(request):
    print(1)
    users=User.objects.all()
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    for i in users:
        time=i.upload_time
        list1=str(time).split('-')
        print(list1[1])
        if list1[1]=='01':
            count1+=1
        elif list1[1]=='02':
            count2+=1
        elif list1[1]=='03':
            count3+=1
        elif list1[1]=='04':
            count4+=1
        elif list1[1]=='05':
            count5+=1
        elif list1[1]=='06':
            count6+=1

    x=['1月','2月','3月','4月','5月','6月']
    print(count1,count2,count3,count4,count5,count6)
    y=[count1,count2,count3,count4,count5,count6]
    data={
        'x':x,
        'y':y,
    }
    return JsonResponse(data,safe=False)


@cache_page(timeout=100,key_prefix='cacheRedis')
def get_map(request):
    data=[]
    city = ["北京", "天津", "河北", "山西", "内蒙古", "吉林", "黑龙江", "辽宁", "上海", "江苏", "浙江", "安徽",
                     "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州", "云南", "西藏",
                     "陕西", "甘肃", "青海", "宁夏", "新疆", "香港", "澳门", "台湾"
                     ]
    for i in city:
        data.append({"name":i,"value":len(User.objects.filter(address=i))})

    # data=[
    #     {"name":'北京',"value":value1},
    #     {"name":'四川',"value":value2},
    #     {"name":'重庆',"value":value3},
    #     {"name":'新疆',"value":value4},
    # ]
    return JsonResponse(data,safe=False)