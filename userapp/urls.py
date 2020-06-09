
from django.contrib import admin
from django.urls import path
from userapp import views
app_name='userapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_all_data/',views.get_all_data,name='get_all_data'),
    path('ban_user/',views.ban_user,name='ban_user'),
    path('get_data/',views.get_data,name='get_data'),
    path('get_map/',views.get_map,name='get_map')

]
