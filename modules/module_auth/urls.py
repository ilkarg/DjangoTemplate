from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RouteRegisterUser.as_view()),
    path('login/', views.RouteLoginUser.as_view()),
    path('logout/', views.RouteLogoutUser.as_view())
]
