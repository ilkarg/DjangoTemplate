from django.urls import path
from modules.module_auth import views

urlpatterns = [
    path('register/', views.ViewRegisterUser.as_view()),
    path('login/', views.ViewLoginUser.as_view()),
    path('logout/', views.ViewLogoutUser.as_view())
]
