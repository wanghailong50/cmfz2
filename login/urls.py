
from django.contrib import admin
from django.urls import path,include
from login import views
app_name='login'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/',views.page,name='page'),
    path('get_code/',views.get_code,name='get_code'),
    path('verify/',views.verify_code,name='verify_code')
]
