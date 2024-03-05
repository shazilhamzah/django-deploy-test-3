from django.contrib import admin
from django.urls import path,include
from home.views import home,user_login,register,userhome,user_logout

urlpatterns = [
    path('',home,name='home'),
    path('login/',user_login,name='login'),
    path('register/',register,name='register'),
    path('userhome/',userhome,name='userhome'),
    path('logout/',user_logout,name='user_logout')
]   
