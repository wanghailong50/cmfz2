
from django.contrib import admin
from django.urls import path,include
from indexapp import views
app_name='index'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/',views.page,name='page'),
    path('add_banner/',views.add_banner,name='add_banner'),
    path('get_all_data/',views.get_all_data,name='get_all_data'),
    path('data/',views.data,name='data'),
    path('change_banner/',views.change_banner,name='change_banner')
]
