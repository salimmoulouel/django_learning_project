from django.urls import path,include
from basic_app import views
from django.contrib import admin

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('',views.index,name='index'),
    
    path('register/',views.register,name='register'),
    
    
    path('admin/',admin.site.urls),
    path("login/",views.user_login,name='user_login')

]
