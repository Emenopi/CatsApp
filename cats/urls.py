from django.urls import path
from cats import views

app_name = 'cats'

urlpatterns = [
    path('', views.index, name='index'),
    path('cats_list/', views.cats_list, name='cats'),
    path('cats/<slug:student_name_slug>', views.show_student_profile, name="student_profile"),
    path('cats/<slug:cat_slug>/', views.show_cat_profile, name='cat_profile'),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('add_cat/', views.add_cat, name="add_cat"),
]