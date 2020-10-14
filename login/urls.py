from django.urls import path
from .views import index, login, register, spider
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index, name="home"),
    path('register/', register, name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('spider/', spider, name="spider_page"),
]