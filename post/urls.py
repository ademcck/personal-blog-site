from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'post'
urlpatterns = [
    path('index',post_index ,name='index'),
    path('create',post_create, name='create'),
    path('<slug:slug>/detail',post_detail, name='detail'),
    path('<slug:slug>/update',post_update, name='update'),
    path('<slug:slug>/delete',post_delete, name='delete'),
    path('category/<str:cats>/',category_view, name='category'),
    path('like/<int:pk>',like_view, name='like_post'),
    path('liked-posts/',liked_view, name='liked_posts'),
]

