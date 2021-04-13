from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from loginapp.models import TStu, TAdmin, TTeacher


def login(request):
    return render(request, 'login.html')


def login_logic(request):
    # 获取登陆信息
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    auth = request.POST.get('authority')
    #print(auth)

    # 判断所属权限
    # 管理员
    if auth == "admin":
        # 返回一个QuerySet,其中是满足条件的数据
        # 可以有多条数据，如果没有数据，就返回一个空白的QuerySet
        admin = TAdmin.objects.filter(admin_id=username, password=pwd)
        #print(admin)
        # 判断账户密码
        if admin:
            # 设置登录状态
            request.session['login'] = username
            return render(request, 'homepage/admin_homepage.html')

    # 学生
    if auth == "stu":
        stu = TStu.objects.filter(stu_id=username, password=pwd)
        #print(stu)
        # 判断账户密码
        if stu:
            # 设置登录状态
            request.session['login'] = username
            return render(request, 'homepage/stu_homepage.html')

    # 教师
    if auth == "teacher":
        teacher = TTeacher.objects.filter(teacher_id=username, password=pwd)
        #print(teacher)
        # 判断账户密码
        if teacher:
            # 设置登录状态
            request.session['login'] = username
            return render(request, 'homepage/teacher_homepage.html')
