
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), # Main page
    path('group/<slug:slug>/', views.group_posts), #
]