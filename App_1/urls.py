from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('forum_page/', views.forum_page, name='forum_page'),
    path('site_news/', views.site_news, name='news_page'),
    path('record_creation_page/', views.creating_record_views, name='record_creation_page'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
