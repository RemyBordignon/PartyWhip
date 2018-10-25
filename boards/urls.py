from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('new_bid/<int:post_id>/', views.create_bid, name='create_bid'),
    path('new_post/', views.create_post, name='create_post'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('my_bids/', views.my_bids, name='my_bids'),
    path('winner_selected/<int:bid_id>/', views.set_winner_selected, name='winner_selected'),
    path('search/', views.search, name='search'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post')
]
