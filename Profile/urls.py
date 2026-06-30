from django.urls import path
from . import views
app_name='Profile'
urlpatterns = [
    path('register',views.RegisterView,name="Register"),
    path('login',views.LoginView,name="login"),
    path('dashboard',views.Dashboard,name="dashboard"),
    path('logout',views.Logout,name="logout")
]
