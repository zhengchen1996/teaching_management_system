from django.urls import path

from examapp import views

app_name = 'examapp'
urlpatterns = [
    path('admin_exam/', views.getdata_exam, name='admin_exam'),
    path('add_exam/', views.add_exam, name='add_exam'),
    path('addlogic_exam/', views.addlogic_exam, name='addlogic_exam'),
    path('alter_exam/', views.alter_exam, name='alter_exam'),
    path('alterlogic_exam/', views.alterlogic_exam, name='alterlogic_exam'),
    path('stu_exam/', views.stu_exam, name='stu_exam'),
    path('teacher_classexam/', views.teacher_classexam, name='teacher_classexam'),
    path('teacher_invigilate/', views.teacher_invigilate, name='teacher_invigilate'),
    path('admin_gradeexam/', views.getdata_gradeexam, name='admin_gradeexam'),
    path('add_gradeexam/', views.add_gradeexam, name='add_gradeexam'),
    path('addlogic_gradeexam/', views.addlogic_gradeexam, name='addlogic_gradeexam'),
    path('alter_gradeexam/', views.alter_gradeexam, name='alter_gradeexam'),
    path('alterlogic_gradeexam/', views.alterlogic_gradeexam, name='alterlogic_gradeexam'),
    path('stu_grade_sign/', views.stu_grade_sign, name='stu_grade_sign'),
    path('stu_signlogic_grade/', views.stu_signlogic_grade, name='stu_signlogic_grade'),
    path('stu_grade_signed/', views.stu_grade_signed, name='stu_grade_signed'),
]