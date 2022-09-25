from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('gallery',views.gallery,name="gallery"),
    path('attendance',views.attendance,name="attendance"),
    path('about',views.about,name="about"),
    path('achievements',views.achievements,name="achievements"),
    path('biceps/',views.biceps),
    path('back/',views.back),
    path('shoulders/',views.shoulders),
    path('chest/',views.chest),
    path('abs/',views.abs),
    path('legs/',views.legs),
    path('yoga/',views.yoga),
    path('products/',views.products),




    
]
