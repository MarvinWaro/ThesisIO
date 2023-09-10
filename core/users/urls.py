from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_landing, name='welcome_landing'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
]