from django.urls import path

from classapp import views

app_name = 'classapp'
urlpatterns = [
    path('admin_class/', views.getdata_class, name='admin_class'),
    path('add_class/', views.add_class, name='add_class'),
    path('addlogic_class/', views.addlogic_class, name='addlogic_class'),
    path('alter_class/', views.add_class, name='alter_class'),
    path('alterlogic_class/', views.add_class, name='alterlogic_class'),
    path('stu_schedule/', views.stu_schedule, name='stu_schedule'),
    path('stu_class_select/', views.stu_class_select, name='stu_class_select'),
    path('stu_selectlogic_class/', views.stu_selectlogic_class, name='stu_selectlogic_class'),
    path('stu_class_selected/', views.stu_class_selected, name='stu_class_selected'),
    path('teacher_class/', views.teacher_class, name='teacher_class'),

]