from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.wordhome,name="wordhome"),
    path('detail/',views.worddetail,name="worddetail"),
    path('result/',views.wordresult,name="wordresult"),
]