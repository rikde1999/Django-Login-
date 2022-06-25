from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.INDEX),
    
    path('add',views.ADD),
    path('edit',views.EDIT),
    path('update/<int:id>',views.Update),
    path('delete',views.DELETE),
]