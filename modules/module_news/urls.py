from django.urls import path
from . import views

urlpatterns = [
    path('load_all_news/', views.ViewLoadAllNews.as_view()),
    path('add_news/', views.ViewAddNews.as_view()),
    path('load_news/<id>', views.ViewLoadNews.as_view())
]
