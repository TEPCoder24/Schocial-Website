from django.urls import path
from . import views

urlpatterns = [
	path("home/", views.home_page_load, name="home"),
	path("user/", views.user_page_load, name="user"),
	path("login/", views.login_page_load, name="login"),
    path("logout/", views.logout_user, name="logout"),
	path("signup/", views.signup_page_load, name="signup"),
	path("", views.welcome_page_load, name="welcome"),
    path("closed/", views.closed_site, name="closed"),
]
