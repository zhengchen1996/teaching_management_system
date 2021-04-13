from django.urls import path

from teachapp import views

app_name = 'teachapp'
urlpatterns = [
    path('admin_teach/', views.getdata_teach, name='admin_teach'),
    path('add_teach/', views.add_teach, name='add_teach'),
    path('addlogic_teach/', views.addlogic_teach, name='addlogic_teach'),
    path('alter_teach/', views.alter_teach, name='alter_teach'),
    path('alterlogic_teach/', views.alterlogic_teach, name='alterlogic_teach'),
    path('stu_teach/', views.stu_teach, name='stu_teach'),
    path('stu_teach_details/', views.stu_teach_details, name='stu_teach_details'),
    path('teacher_teach/', views.teacher_teach, name='teacher_teach'),
]