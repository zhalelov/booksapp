from django.contrib import admin
from django.urls import path, include
from .views import about

urlpatterns = [
    path('about/', about),
    path('admin/', admin.site.urls),
    path('', include('booksapp.urls')),
]
