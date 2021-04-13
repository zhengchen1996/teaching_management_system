from django.urls import path

from scoreapp import views

app_name = 'scoreapp'
urlpatterns = [
    path('stu_score/', views.stu_score, name="stu_score"),
    path('teacher_score/', views.getdata_score, name="teacher_score"),
    path('add_score/', views.add_score, name="add_score"),
    path('addlogic_score/', views.addlogic_score, name="addlogic_score"),
]