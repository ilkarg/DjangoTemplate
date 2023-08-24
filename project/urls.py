from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('modules.module_news.urls')),
    path('auth/', include('modules.module_auth.urls'))
]
