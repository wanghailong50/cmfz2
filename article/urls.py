
from django.contrib import admin
from django.urls import path
from article import views
app_name='article'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_article/',views.get_article,name='get_article'),
    path('upload_img/',views.upload_img,name='upload_img'),
    path('get_img/',views.get_img,name='get_img'),
    path('add_article/',views.add_article,name='add_article'),
    path('change_article/',views.change_article,name='change_article'),
    path('del_data/',views.del_data,name='del_data')
]
