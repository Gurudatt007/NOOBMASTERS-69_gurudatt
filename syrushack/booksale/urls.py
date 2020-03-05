from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name= 'signup'),
    path('signup/login.html',views.login,name= 'login'),
];