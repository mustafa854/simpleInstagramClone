from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.signin, name='signin'),
    path('accounts/register/', views.signup, name='signup'),
    path('accounts/logout/', views.logout_view, name='logout'),
    ]
        