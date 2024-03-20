from django.urls import path
from cats import views

app_name = 'cats'

urlpatterns = [
    path('', views.index, name='index'),
    path('cats_list/', views.cats_list, name='cats'),
    path('cats/<slug:cat_slug>/', views.show_cat_profile, name='cat_profile'),
]