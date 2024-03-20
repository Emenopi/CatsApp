from django.urls import path
from cats import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('cats_list/', views.cats_list, name='cats_list'),
]