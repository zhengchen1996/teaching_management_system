from django.shortcuts import render
# Create your views here.
from loginapp.models import TAdmin, TStu, TTeacher


# 向页面输出数据
# 跳转管理员信息页面（管理员）
def getdata_admin(request):
    adlist = TAdmin.objects.all()
    print(adlist)
    return render(request, 'personal_infor/admin_admin.html', {'list': adlist})


# 跳转增加管理员页面（管理员）
def add_admin(request):
    return render(request, 'personal_infor/admin_add_admin.html')


# 增加管理员（管理员）
def addlogic_admin(request):
    # 获取表单输入信息
    username = request.POST.get('admin_id')
    pwd = request.POST.get('password')
    name = request.POST.get('name')
    sex = request.POST.get('gender')
    if sex == 'male':
        sex = '男'
    else:
        sex = '女'
    tel = request.POST.get('tel')
    print(username, pwd, name, sex, tel)
    TAdmin.objects.create(admin_id=username, password=pwd, name=name, sex=sex, telephone=tel)
    return getdata_admin(request)


# 跳转修改管理员页面（管理员）
def alter_admin(request):
    return render(request, 'personal_infor/admin_alter_admin.html')


# 修改管理员（管理员）
def alterlogic_admin(request):
    return render(request, 'personal_infor/admin_admin.html')


# 向页面输出数据
# 跳转学生信息页面（管理员）
def getdata_stu(request):
    stulist = TStu.objects.all()
    print(stulist)
    return render(request, 'personal_infor/admin_stu.html', {'list': stulist})


# 跳转增加学生页面（管理员）
def add_stu(request):
    return render(request, 'personal_infor/admin_add_stu.html')


# 增加学生（管理员）
def addlogic_stu(request):
    # 获取表单输入信息
    username = request.POST.get('stu_id')
    pwd = request.POST.get('password')
    name = request.POST.get('name')
    sex = request.POST.get('gender')
    if sex == 'male':
        sex = '男'
    else:
        sex = '女'
    native = request.POST.get('native')
    birth = request.POST.get('birth')
    entrance = request.POST.get('entrance')
    academy = request.POST.get("academy")
    if academy == 'xx':
        academy = 'xx'
    major = request.POST.get("major")
    if major == 'xx':
        major = 'xx'
    scalss = request.POST.get("sclass")
    if scalss == 'xx':
        scalss = 'xx'
    tel = request.POST.get('tel')
    print(username, pwd, name, sex, native, birth, entrance, academy, major, scalss, tel)
    TStu.objects.create(stu_id=username, password=pwd, name=name, sex=sex, native=native,
                          birthday=birth, entrance=entrance, academy=academy, major=major,
                          scalss=scalss, telephone=tel)
    return getdata_stu(request)


# 跳转修改学生页面（管理员）
def alter_stu(request):
    return render(request, 'personal_infor/admin_alter_stu.html')


# 修改学生（管理员）
def alterlogic_stu(request):
    return render(request, 'personal_infor/admin_stu.html')


# 向页面输出数据
# 跳转教师信息页面（管理员）
def getdata_teacher(request):
    teacherlist = TTeacher.objects.all()
    print(teacherlist)
    return render(request, 'personal_infor/admin_teacher.html', {'list': teacherlist})


# 跳转增加教师页面（管理员）
def add_teacher(request):
    return render(request, 'personal_infor/admin_add_teacher.html')


# 增加教师（管理员）
def addlogic_teacher(request):
    # 获取表单输入信息
    username = request.POST.get('teacher_id')
    pwd = request.POST.get('password')
    name = request.POST.get('name')
    sex = request.POST.get('gender')
    if sex == 'male':
        sex = '男'
    elif sex == 'female':
        sex = '女'
    native = request.POST.get('native')
    birth = request.POST.get('birth')
    diplomas = request.POST.get('diplomas')
    politics = request.POST.get('politics')
    if politics == 'mass':
        politics = '群众'
    elif politics == 'party_member':
        politics = '党员'
    elif politics == 'probationary':
        politics = '预备党员'
    entrance = request.POST.get('entrance')
    job = request.POST.get("job")
    academy = request.POST.get("academy")
    if academy == 'xx':
        academy = 'xx'
    tel = request.POST.get('tel')
    print(username, pwd, name, sex, native, birth, diplomas, politics, entrance, academy, job, tel)
    TTeacher.objects.create(teacher_id=username, password=pwd, name=name, sex=sex, native=native,
                          birthday=birth, diplomas=diplomas, politics=politics,
                          entrance=entrance, job_title=job, academy=academy, telephone=tel)
    return getdata_teacher(request)


# 跳转修改教师页面（管理员）
def alter_teacher(request):
    return render(request, 'personal_infor/admin_alter_teacher.html')


# 修改教师（管理员）
def alterlogic_teacher(request):
    return render(request, 'personal_infor/admin_teacher.html')


# 修改密码页面（管理员）
def alterpwd_admin(request):
    return render(request, 'personal_infor/admin_alter_password.html')


# 修改密码逻辑（管理员） ？？是否跳转修改成功页面
def alterlogic_pwd_admin(request):
    return render(request, 'personal_infor/admin_admin.html')


# 学生个人信息页面（学生）
def stu_infor(request):
    return render(request, 'personal_infor/stu_infor.html')


# 修改密码页面（学生）
def alterpwd_stu(request):
    return render(request, 'personal_infor/stu_alter_password.html')


# 修改密码逻辑（学生）？？是否跳转修改成功页面
def alterlogic_pwd_stu(request):
    return render(request, 'personal_infor/stu_infor.html')


# 教师个人信息页面（教师）
def teacher_infor(request):
    return render(request, 'personal_infor/teacher_infor.html')


# 修改密码页面（教师）
def alterpwd_teacher(request):
    return render(request, 'personal_infor/teacher_alter_password.html')


# 修改密码逻辑（教师）？？是否跳转修改成功页面
def alterlogic_pwd_teacher(request):
    return render(request, 'personal_infor/teacher_infor.html')