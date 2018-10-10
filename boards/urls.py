from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('new_bid/', views.create_bid, name='create_bid'),
    path('new_post/', views.create_post, name='create_post'),
]
