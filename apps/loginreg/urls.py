from django.conf.urls import url
from django.contrib import admin
from . import views
#loginreg
urlpatterns = [
    url(r'^login', views.index,name='index'),
    url(r'^return$',views.login,name='login'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^registration$',views.registration,name='register')
]
