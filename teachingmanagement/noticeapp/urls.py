from django.urls import path

from noticeapp import views

app_name = 'noticeapp'
urlpatterns = [
    path('admin_notice/', views.getdata_notice, name='admin_notice'),
    path('add_notice/', views.add_notice, name='add_notice'),
    path('addlogic_notice/', views.addlogic_notice, name='addlogic_notice'),
    path('alter_notice/', views.alter_notice, name='alter_notice'),
    path('alterlogic_class/', views.alterlogic_class, name='alterlogic_class'),
    path('stu_notice/', views.stu_notice, name='stu_notice'),
    path('teacher_notice/', views.teacher_notice, name='teacher_notice'),

]