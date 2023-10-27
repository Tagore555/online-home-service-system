from django.urls import path
from . import views
from django_otp import views as otp_views





urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),
    path('',views.home,name="home"),
    path('services/',views.services,name="services"), 
    path('feedback/',views.feedback,name="feedback"),
    path('employee/',views.employee,name="employee"),    
]