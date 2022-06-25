from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('data',views.data,name='home'),
    path('delete/<int:id>',views.delete_data),
    path('update/<int:id>',views.update_page),
    path('updatenow',views.update),

]
