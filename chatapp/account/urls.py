from django.urls import path
from .views import *

app_name = 'account' 
urlpatterns = [
    path("login/",LoginView.as_view(),name="login") ,
    path("register/",RegisterView.as_view(),name="register") ,
    path("logout/" , LogoutView.as_view() , name="logout" ) ,
    path("profile/<str:username>/" , ProfileView.as_view() , name="profile") ,
    path("editprofile/<str:username>/" , EditProfileView.as_view() , name="editprofile") ,

]