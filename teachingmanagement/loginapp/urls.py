from django.urls import path
from loginapp import views


app_name = 'loginapp'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('loginlogic/', views.login_logic, name='loginlogic'),
]