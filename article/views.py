from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
from article.models import Article
from article.models import Img
import json
# Create your views here.


def get_article(request):
    article=Article.objects.all()
    num = request.GET.get('rows')  # 每页数量
    page = request.GET.get('page')  # 当前页码
    # 进行分页
    all_page = Paginator(article, num)
    # 获取每一页对象
    try:
        student_page = all_page.page(page).object_list
    except:
        student_page = all_page.page(page-1).object_list
    data = {
        "page": page,  # 页码
        "total": all_page.num_pages,  # 总页数
        "records": all_page.count,  # 总条数
        "rows": list(student_page)  # 分页后的每一页的对象
    }

    def mydefalut(u):
        if isinstance(u, Article):
            return {'id': u.id, 'title': u.title.name, 'upload_time': str(u.upload_time), 'status': str(u.status),
                    'pulish_time': str(u.pulish_time),'content':str(u.content)}

    result = json.dumps(data, default=mydefalut)

    return HttpResponse(result)


@csrf_exempt
def upload_img(request):
    image=request.FILES.get('imgFile')
    if image:
        img_url=request.scheme+'://'+request.get_host()+'/static/pic/'+str(image)
        Img.objects.create(img=image)
        result={"error": 0, "url": img_url}
    else:
        result = {"error": 500, "url": "图片上传失败"}
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_img(request):
    pic_url = request.scheme + "://" + request.get_host() + "/static/"
    pic_list = Img.objects.all()
    rows = []
    for item in list(pic_list):
        # 获取文件的后缀名
        path, pic_suffix = os.path.splitext(item.img.url)
        rows.append(
            {"is_dir": False,
             "has_file": False,
             "filesize": item.img.size,
             "dir_path": "",
             "is_photo": True,
             "filetype": pic_suffix,
             "filename": item.img.name,
             "datetime": "2018-06-06 00:36:39"},
        )
    # current_url 与 filename
    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": pic_url,  # 图片空间的路径
        "total_count": len(pic_list),  # 图片的总数
        # 所有图片的属性
        "file_list": rows
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def add_article(request):
    title=request.GET.get('title1')
    category = request.GET.get("category1")
    content = request.GET.get("content1")
    result=Article.objects.create(title=title,content=content,status=category)
    if result:
        data={"msg":"success"}
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        data={"msg":"no"}
        return HttpResponse(json.dumps(data), content_type="application/json")


def change_article(request):
    id=request.GET.get('get_id')
    title = request.GET.get('title')
    category = request.GET.get("category")
    content = request.GET.get("content")
    result=Article.objects.filter(id=id)[0]
    if result:
        result.title=title
        result.content=content
        result.status=category
        result.save()
    return HttpResponse('success')


def del_data(request):
    id=request.GET.get('data')
    print(id)
    # 查询id，删除数据
    try:
        result = Article.objects.filter(id=id)[0]
        result.delete()
    except:
        pass
    return HttpResponse('success')