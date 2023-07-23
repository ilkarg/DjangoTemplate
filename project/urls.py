from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('load_all_news/', views.RouteLoadAllNews.as_view()),
    path('add_news/', views.RouteAddNews.as_view()),
    path('load_news/<id>', views.RouteLoadNews.as_view()),
    path('register/', views.RouteRegisterUser.as_view()),
    path('login/', views.RouteLoginUser.as_view()),
    path('logout/', views.RouteLogoutUser.as_view())
]