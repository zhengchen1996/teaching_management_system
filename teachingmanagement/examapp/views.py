from django.shortcuts import render

# Create your views here.
from loginapp.models import TExam, TGradeExam


# 转向考务管理信息页面（管理员）
def getdata_exam(request):
    examlist = TExam.objects.all()
    print(examlist)
    return render(request, 'exam/admin_exam.html', {'list': examlist})


# 跳转增加考务页面（管理员）
def add_exam(request):
    return render(request, 'exam/admin_add_exam.html')


# 增加考务（管理员）
def addlogic_exam(request):
    # 获取表单输入信息
    class_id = request.POST.get('class_id')
    class_name = request.POST.get('class_name')
    time = request.POST.get('time')
    place = request.POST.get('place')
    number = request.POST.get('number')
    teacher = request.POST.get('teacher')
    print(class_id, class_name, time, place, number, teacher)
    TExam.objects.create(class_id=class_id, time=time, place=place, teacher_id=teacher)
    return getdata_exam(request)


# 跳转修改考务页面（管理员）
def alter_exam(request):
    return render(request, 'exam/admin_alter_exam.html')


# 修改考务逻辑（管理员）
def alterlogic_exam(request):
    return render(request, 'exam/admin_exam.html')


# 查询考试信息（学生）
def stu_exam(request):
    return render(request, 'exam/stu_exam_arrange.html')


# 查询任课课程考试信息（教师）
def teacher_classexam(request):
    return render(request, 'exam/teacher_class_exam.html')


# 查询监考科目（教师）
def teacher_invigilate(request):
    return render(request, 'exam/teacher_invigilate.html')


# 转向等级考试管理信息页面（管理员）
def getdata_gradeexam(request):
    gradeexamlist = TGradeExam.objects.all()
    print(gradeexamlist)
    return render(request, 'exam/admin_gradeexam.html', {'list': gradeexamlist})


# 跳转增加等级考试页面（管理员）
def add_gradeexam(request):
    return render(request, 'exam/admin_add_gradeexam.html')


# 增加等级考试（管理员）
def addlogic_gradeexam(request):
    # 获取表单输入信息
    grade_id = request.POST.get('grade_id')
    name = request.POST.get('name')
    exam_time = request.POST.get('exam_time')
    end_time = request.POST.get('end_time')
    number = request.POST.get('number')
    print(grade_id, name, exam_time, end_time, number)
    TGradeExam.objects.create(grade_id=grade_id, name=name, exam_time=exam_time, end_time=end_time)
    return getdata_gradeexam(request)


# 跳转修改等级考试页面（管理员）
def alter_gradeexam(request):
    return render(request, 'exam/admin_alter_gradeexam.html')


# 修改等级考试逻辑（管理员）
def alterlogic_gradeexam(request):
    return render(request, 'exam/admin_gradeexam.html')


# 跳转报名等级考试信息页面（学生）
def stu_grade_sign(request):
    return render(request, 'exam/stu_signup.html')


# 报名逻辑（学生）
def stu_signlogic_grade(request):
    return render(request, 'exam/stu_signup.html')


# 跳转已报等级考试信息页面（学生）
def stu_grade_signed(request):
    return render(request, 'exam/stu_signed.html')
