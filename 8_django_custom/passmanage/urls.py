from django.urls import path, include
from . import views

urlpatterns = [
    # /password-manager/
    path('', views.Home.as_view(), name="home"),
    # /password-manager/login
    path('login/', views.Login.as_view(), name="login"),
    # /password-manager/register
    path('register/', views.Register.as_view(), name="register"),
    # /password-manager/dashboard
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    # # Adds a bunch of URLs (password-manager/accounts/login, etc.)
    # path('accounts/', include('django.contrib.auth.urls')),
]
