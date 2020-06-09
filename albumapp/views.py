import json

from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from albumapp.models import Album,Chapter
# Create your views here.


def get_AllAlbum(request):
    album=Album.objects.all()

    num = request.GET.get('rows')  # 每页数量
    page = request.GET.get('page')  # 当前页码
    # 进行分页
    all_page = Paginator(album, num)
    # 获取每一页对象
    try:
        student_page = all_page.page(page).object_list
    except:
        student_page = all_page.page(page - 1).object_list
    data = {
        "page": page,  # 页码
        "total": all_page.num_pages,  # 总页数
        "records": all_page.count,  # 总条数
        "rows": list(student_page)  # 分页后的每一页的对象
    }

    def mydefalut(u):
        if isinstance(u, Album):
            return {'id': u.id, 'title': u.name.name, 'grade': str(u.grade), 'author': str(u.author),
                    'play_people': u.play_people.name, 'number': u.number.name,'content':u.content,'status':u.ready,'pulish_time':str(u.pulish_time)}

    result = json.dumps(data, default=mydefalut)

    return HttpResponse(result)


def get_all_chapter(request):
    id=request.GET.get('id')
    chapter=Chapter.objects.filter(album_id=id)
    num = request.GET.get('rows')  # 每页数量
    page = request.GET.get('page')  # 当前页码
    # 进行分页
    all_page = Paginator(chapter, num)
    # 获取每一页对象
    try:
        student_page = all_page.page(page).object_list
    except:
        student_page = all_page.page(page - 1).object_list
    data = {
        "page": page,  # 页码
        "total": all_page.num_pages,  # 总页数
        "records": all_page.count,  # 总条数
        "rows": list(student_page)  # 分页后的每一页的对象
    }

    def mydefalut(u):
        if isinstance(u, Chapter):
            return {'id': u.id, 'title': u.chapter_name.name, 'size': str(u.size),'url':u.chapter.name
                    }

    result = json.dumps(data, default=mydefalut)


    return HttpResponse(result)


@csrf_exempt
def change_data(request):
    oper=request.POST.get('oper')
    if oper == 'del':
        id = request.POST.get('id')
        print(id,type(id))
        reslut = Album.objects.filter(id=int(id))
        reslut.delete()

    elif oper == 'edit':
        id=request.POST.get('id')
        title = request.POST.get('title')
        grade = request.POST.get('grade')
        author = request.POST.get('author')
        play_people = request.POST.get('play_people')
        number = request.POST.get('number')
        content = request.POST.get('content')
        status = request.POST.get('status')

        pulish_time = request.POST.get('pulish_time')
        result=Album.objects.filter(id=id)[0]
        result.name=title
        result.grade=grade
        result.author=author
        result.play_people=play_people
        result.number=number
        result.content=content
        result.ready=status

        puslish = datetime.date(*map(int, pulish_time.split('-')))  #转化为datatime类型进行存储
        result.pulish_time = puslish
        result.save()

    elif oper=='add':
        title = request.POST.get('title')
        grade = request.POST.get('grade')
        author = request.POST.get('author')
        play_people = request.POST.get('play_people')
        number = request.POST.get('number')
        content = request.POST.get('content')
        status = request.POST.get('status')
        pulish_time = request.POST.get('pulish_time')

        Album.objects.create(pulish_time=pulish_time,name=title,grade=grade,author=author,play_people=play_people,
                             number=number,content=content,ready=status,)

    return HttpResponse()


def del_chapter(request):
    id=request.GET.get('data')
    try:
        reslut=Chapter.objects.get(id=id)
        reslut.delete()
        return HttpResponse('success')
    except:
        return HttpResponse('faild')


@csrf_exempt
def add_chapter(request):
    row_id=request.GET.get('row_id')

    chapter_name=request.POST.get('chapter_name')
    file=request.FILES.get('file')
    Chapter.objects.create(chapter_name=chapter_name,chapter=file,album_id=row_id)
    return HttpResponse('1')


@csrf_exempt
def change_chapter(request):
    row_id=request.GET.get('row_id')
    file=request.FILES.get('file')
    title=request.POST.get('title')
    result=Chapter.objects.filter(id=row_id)[0]
    result.chapter_name=title
    result.chapter=file
    result.save()
    return HttpResponse('1')