from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('new_invitation/', views.create_post, name='create_post')
]