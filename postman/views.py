from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from albumapp.models import Album, Chapter
from article.models import Article
from indexapp.models import Slides
from login.models import User
from postman.models import Change
# Create your views here.


def first_page(request):
    uid=request.GET.get('uid')
    type=request.GET.get('type')
    sub_type=request.GET.get('sub_type')

    result=''
    if not uid:
        result={"status": 500, "message": "用户不存在"}
        return JsonResponse(result)

    if type=='all':
        # 轮播图，专辑  文章
        slides = Slides.objects.all()
        header=[]
        for slide in slides:
            header.append({"desc":slide.titile.name,
                           'id':slide.id,
                           "thumbnail":'http://127.0.0.1:8000/static/'+slide.img.name})


        #     专辑
        album = Album.objects.all()
        album_list=[]
        for alb in album:
            album_list.append({
                "thumbnail": alb.play_people.name,#播音
                "title": alb.name.name,	#//标题
                "author": alb.author.name,#		//描述
                "type": "0",	#//类型（0：闻，1：思）
                "set_count": alb.number.name, #	//集数（只有闻的数据才有）
                "create_date": str(alb.pulish_time) #	//创建时间
                    }
            )

        #     文章
        article_list=[]
        if sub_type=='xfmy':

            article = Article.objects.filter(status=1)
            print(article)
            for art in article:
                article_list.append({
                    "thumbnail": art.img.name,
                    "title": art.title.name,
                    "author": art.title.name,
                    "type": "0",
                    "set_count": "",
                    "create_date": str(art.pulish_time)
                    }
                )
        else:
            article = Article.objects.filter(status=0)
            for art in article:
                article_list.append({
                    "thumbnail": art.img.name,
                    "title": art.title.name,
                    "author": art.title.name,
                    "type": "1",
                    "set_count": "",
                    "create_date": str(art.pulish_time)
                    }
                )



        result={
            "header":header,
            "album":album_list,
            "artical":article_list
    }

    elif type=='wen':
        #     专辑
        album = Album.objects.all()
        album_list = []
        for alb in album:
            album_list.append({
                "thumbnail": alb.play_people.name,  # 播音
                "title": alb.name.name,  # //标题
                "author": alb.author.name,  # //描述
                "type": "0",  # //类型（0：闻，1：思）
                "set_count": alb.number.name,  # //集数（只有闻的数据才有）
                "create_date": str(alb.pulish_time)  # //创建时间
            }
            )
        result = {
            "header": [],
            "album": album_list,
            "artical": []
        }
    elif type=='si':
        article_list = []
        print(sub_type)
        if sub_type == 'xfmy':
            article = Article.objects.filter(status=1)
            print(article)
            for art in article:
                article_list.append({
                    "thumbnail": art.img.name,
                    "title": art.title.name,
                    "author": art.title.name,
                    "type": "0",
                    "set_count": "",
                    "create_date": str(art.pulish_time)
                }
                )
                result = {
                    "header": [],
                    "album": [],
                    "artical": article_list
                }
        else:
            article = Article.objects.filter(status=0)
            for art in article:
                article_list.append({
                    "thumbnail": art.img.name,
                    "title": art.title.name,
                    "author": art.title.name,
                    "type": "1",
                    "set_count": "",
                    "create_date": str(art.pulish_time)
                }
                )

            result = {
                "header": [],
                "album": [],
                "artical": article_list
            }

    return JsonResponse(result,safe=False)


def album_detail(request):
    id=request.GET.get('id')
    uid=request.GET.get('uid')
    if not id or not uid:
        result = {"status": 500, "message": "用户不存在"}
        return JsonResponse(result)
    # 获取指定专辑的数据
    album = Album.objects.filter(id=id)
    # 获取该专辑的其他详情资料
    chapters = Chapter.objects.filter(album_id=id)
    album_list = []
    chapter_list=[]
    for alb in album:
        album_list.append({
            "thumbnail": alb.play_people.name,  # 播音
            "title": alb.name.name,  # //标题
            "author": alb.author.name,  # //描述
            "type": "0",  # //类型（0：闻，1：思）
            "set_count": alb.number.name,  # //集数（只有闻的数据才有）
            "create_date": str(alb.pulish_time)  # //创建时间
        }
        )
    for chapter in chapters:
        chapter_list.append(
            {
                "title": chapter.url.name, #// 第几集
                "download_url": chapter.chapter.name, # // 下载地址
                "size": chapter.size.name+"kb", # // 音频大小（字节数）
                "duration": chapter.audio #// 音频时长（毫秒数）

        }

        )
    result={
        "introduction": album_list,
            "list": chapter_list
}
    return JsonResponse(result)


@csrf_exempt
def register(request):
    phone=request.POST.get('phone')
    password=request.POST.get('password')
    if not phone or not password:
        result={"status": 500, "message": "用户不存在"}
        return JsonResponse(result)

    rep=User.objects.create(phone=phone)

    user=User.objects.filter(phone=phone)[0]
    if rep:
        result={
            "password": password, #// MD5后的密码
        "uid": user.id, #// 用户的Id
        "phone ": user.phone #// 手机号
        }
    else:
        result={
                "errno": "-200", #// 失败错误码
            "error_msg": "该手机号已经存在" #// 失败提示
        }
    return JsonResponse(result,safe=False)


@csrf_exempt
def change_user(request):
    uid=request.POST.get('uid')
    print(uid)
    password=request.POST.get('password')
    farmington=request.POST.get('farmington')
    nickname=request.POST.get('nickname')
    gender=request.POST.get('gender')
    photo=request.POST.get('photo')
    location=request.POST.get('location')
    province=request.POST.get('province')
    city=request.POST.get('city')
    description=request.POST.get('description')
    phone=request.POST.get('phone')
    if not uid:
        result={"status": 500, "message": "用户不存在"}
        return JsonResponse(result)
    else:
        user = Change.objects.get(id=uid)
        if password:
            user.password = password
        if nickname:
            user.nickname = nickname
        if gender:
            user.gender = gender
        if photo:
            user.photo = photo
        if location:
            user.location = location
        if province:
            user.province = province
        if city:
            user.city = city
        if description:
            user.description = description

        user.save()

        user_age=Change.objects.get(id=uid)
        result = {
            "password": user_age.password,  # //MD5后的密码
            "farmington": user_age.nickname,  # //法名
            "uid": user_age.id,  # //用户id

            "gender": user_age.gender,  # //性别（m：男 f：女）
            "photo": user_age.photo.name,  # //头像
            "location": user_age.location,  # //所在地
            "province": user_age.province,  # //省市
            "city": user_age.city,  # //地区
            "description": user_age.description,  # //个人签名

        }
        return JsonResponse(result,safe=False)


