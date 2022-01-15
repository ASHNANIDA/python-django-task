from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.fnhome, name='home'),
    path('about/', views.fnabout, name='about'),
    path('login/', views.fnlogin, name='login'),
    path('register/', views.fnregister, name='register'),
    path('feedback/', views.fnfeed, name='feedback'),
    path('notification/', views.fnnotif, name='notification'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    ]