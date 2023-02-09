from django.urls import path
from . import views

urlpatterns = [
    # /passmanage/
    path('', views.Home.as_view(), name="home"),
    # /passmanage/login
    path('login/', views.Login.as_view(), name="login"),
    # /passmanage/register
    path('register/', views.Register.as_view(), name="register"),
]
