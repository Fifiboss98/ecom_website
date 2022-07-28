from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

path('signup/', views.sign_up, name="sign_up"),
path('login/', views.login_user, name="login"),
path('logout/', views.logout_user, name="logout")
