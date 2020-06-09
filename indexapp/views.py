from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from indexapp.models import Slides
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def page(request):
    return render(request, 'page.html')


# 添加数据
@csrf_exempt
def add_banner(request):
    title = request.POST.get('title')
    status = request.POST.get('status')
    img = request.FILES.get('img')
    print(title, status, img)
    Slides.objects.create(titile=title, is_show=status, img=img)

    return HttpResponse('success')


# 显示所有数据
def get_all_data(request):
    slides = Slides.objects.all()
    num = request.GET.get('rows')  # 每页数量
    page = request.GET.get('page')  # 当前页码
    # 进行分页
    all_page = Paginator(slides, num)
    # 获取每一页对象
    student_page = all_page.page(page).object_list
    data = {
        "page": page,  # 页码
        "total": all_page.num_pages,  # 总页数
        "records": all_page.count,  # 总条数
        "rows": list(student_page)  # 分页后的每一页的对象
    }

    def mydefalut(u):
        if isinstance(u, Slides):
            return {'id': u.id, 'title': u.titile.name, 'upload_time': str(u.upload_time), 'is_show': str(u.is_show),
                    'pic': str(u.img)}

    result = json.dumps(data, default=mydefalut)

    return HttpResponse(result)


@csrf_exempt
def data(request):
    print(1)
    oper = request.POST.get('oper')
    if oper == 'del':
        id = request.POST.get('id')
        reslut = Slides.objects.filter(id=id)
        reslut.delete()

    elif oper == 'edit':
        print('edit')
        name = request.POST.get('title')
        age = request.POST.get('age')
        classs = request.POST.get('class')
        id = request.POST.get('id')
        print(name)
    return HttpResponse()


@csrf_exempt
def change_banner(request):
    id=request.POST.get('id')
    title = request.POST.get('title')
    status = request.POST.get('status')
    img = request.FILES.get('img')
    print(title, status, img,id)
    result=Slides.objects.filter(id=int(id))[0]
    print(result)
    result.titile=title
    result.img=img
    result.is_show=status
    result.save()

    return HttpResponse('success')