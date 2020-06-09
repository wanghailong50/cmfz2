
from django.contrib import admin
from django.urls import path,include
from postman import views
app_name='postman'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_page/',views.first_page,name='first_page'),
    path('album_detail/',views.album_detail,name='album_detail'),
    path('register/',views.register,name='register'),
    path('change_user/',views.change_user,name='change_user'),
]
