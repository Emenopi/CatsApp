from django.contrib import admin
from django.urls import path, include
from cats import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/', include('cats.urls')),
    path('admin/', admin.site.urls),
]