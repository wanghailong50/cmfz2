
from django.contrib import admin
from django.urls import path
from albumapp import views
app_name='albumapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_AllAlbum/',views.get_AllAlbum,name='get_AllAlbum'),
    path('get_all_chapter/',views.get_all_chapter,name='get_all_chapter'),
    path('change_data/',views.change_data,name='change_data'),
    path('del_chapter/',views.del_chapter,name='del_chapter'),
    path('add_chapter/',views.add_chapter,name='add_chapter'),
    path('change_chapter/',views.change_chapter,name='change_chapter')

]
