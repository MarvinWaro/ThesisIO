from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_landing, name='welcome_landing'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
]