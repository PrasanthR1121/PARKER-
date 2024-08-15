from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('ParkerApp.urls')),
    path('', user_login, name="user_login"),
    path('admin_index/', admin_index, name="admin_index"),
]
