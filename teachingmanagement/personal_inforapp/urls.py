from django.urls import path

from personal_inforapp import views

app_name = 'personal_inforapp'
urlpatterns = [
    path('admin_admin/', views.getdata_admin, name="admin_admin"),
    path('add_admin/', views.add_admin, name='add_admin'),
    path('addlogic_admin/', views.addlogic_admin, name='addlogic_admin'),
    path('alter_admin/', views.alter_admin, name="alter_admin"),
    path('admin_stu/', views.getdata_stu, name="admin_stu"),
    path('add_stu/', views.add_stu, name='add_stu'),
    path('addlogic_stu/', views.addlogic_stu, name='addlogic_stu'),
    path('alter_stu/', views.alter_stu, name="alter_stu"),
    path('admin_teacher/', views.getdata_teacher, name="admin_teacher"),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('addlogic_teacher/', views.addlogic_teacher, name='addlogic_teacher'),
    path('alter_teacher/', views.alter_teacher, name="alter_teacher"),
    path('alterpwd_admin/', views.alterpwd_admin, name='alterpwd_admin'),
    path('alterlogic_pwd_admin/', views.alterlogic_pwd_admin, name='alterlogic_pwd_admin'),
    path('stu_infor/', views.stu_infor, name="stu_infor"),
    path('alterpwd_stu/', views.alterpwd_stu, name="alterpwd_stu"),
    path('alterlogic_pwd_stu/', views.alterlogic_pwd_stu, name="alterlogic_pwd_stu"),
    path('teacher_infor/', views.teacher_infor, name="teacher_infor"),
    path('alterpwd_teacher/', views.alterpwd_teacher, name="alterpwd_teacher"),
    path('alterlogic_pwd_teacher/', views.alterlogic_pwd_teacher, name="alterlogic_pwd_teacher"),

]