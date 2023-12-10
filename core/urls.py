from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index' ),
path('settings/', views.settings, name='settings'),
path('upload-post/', views.uploadPost, name="upload"),   
path('like-post/<int:id>', views.likePost, name="like"),   
path('follow-user/<id>', views.followUser, name="follow"),   
path('<str:username>/', views.profile, name="profile"),   
path('search-user', views.searchUser, name="search"),   
]
