from django.shortcuts import render

# Create your views here.
from loginapp.models import TClass


# 转向课程管理信息页面（管理员）
def getdata_class(request):
    classlist = TClass.objects.all()
    print(classlist)
    return render(request, 'class/admin_class.html', {'list': classlist})


# 跳转增加课程页面（管理员）
def add_class(request):
    return render(request, 'class/admin_add_class.html')


# 增加课程（管理员）
def addlogic_class(request):
    # 获取表单输入信息
    class_id = request.POST.get('class_id')
    name = request.POST.get('name')
    teacher_id = request.POST.get('teacher_id')
    teacher_name = request.POST.get('teacher_name')
    time = request.POST.get('time')
    place = request.POST.get('place')
    week = request.POST.get('week')
    category = request.POST.get('category')
    if category == 'required':
        category = '必修课'
    if category == 'optional':
        category = '选修课'
    academy = request.POST.get('academy')
    if academy == 'xx':
        academy = 'xx'
    credit = request.POST.get('credit')
    print(class_id, name, teacher_id, teacher_name, time, place, week, category, academy, credit)
    TClass.objects.create(class_id=class_id, name=name, teacher_id=teacher_id, time=time,
                          place=place, week=week, category=category, academy=academy, credit=credit)
    return getdata_class(request)


# 跳转修改课程页面（管理员）
def alter_class(request):
    return render(request, 'class/admin_alter_class.html')


# 修改课程逻辑（管理员）
def alterlogic_class(request):
    return render(request, 'class/admin_class.html')


# 跳转学生课表（学生）
def stu_schedule(request):
    return render(request, 'class/stu_schedule.html')


# 跳转学生选课列表（学生）
def stu_class_select(request):
    return render(request, 'class/stu_class_selection.html')


# 选课逻辑（学生）
def stu_selectlogic_class(request):
    return render(request, 'class/stu_class_selection.html')


# 跳转学生已选课程列表（学生）
def stu_class_selected(request):
    return render(request, 'class/stu_class_selected.html')


# 跳转教师所授课程列表（教师）
def teacher_class(request):
    return render(request, 'class/teacher_class.html')
