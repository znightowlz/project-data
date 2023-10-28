from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('homepage', views.homepage, name='homepage'),
    path('login', views.login, name='login')
]