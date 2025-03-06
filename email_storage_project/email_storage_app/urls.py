from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('details/<id>/', views.details, name='details'),
    path('delete/<id>/', views.delete, name='delete'),
    path('update/<id>/', views.update, name='update'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
    path('profile/<id>/', views.profile, name='profile'),
    path('profile-delete/<id>/', views.profile_delete, name='profile_delete'),
    path('download/<id>/', views.download_html_template, name='download_html_template'),
    # path('ratings/<id>/', views.ratings, name='ratings'),
]
