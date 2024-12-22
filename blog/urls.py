
from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('create', views.create, name='create'),
    path('show/<int:blog_id>', views.show, name='show'),
    path('oldredirect/', views.oldredirect, name='oldredirect'),
    path('new_urls/', views.newredirect, name='newredirect')
]