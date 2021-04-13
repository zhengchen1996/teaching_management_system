from django.shortcuts import render

# Create your views here.
from loginapp.models import TNotice


# 转向公告管理页面（管理员）
def getdata_notice(request):
    noticelist = TNotice.objects.all()
    print(noticelist)
    return render(request, 'notice/admin_notice.html', {'list': noticelist})


# 跳转增加公告页面（管理员）
def add_notice(request):
    return render(request, 'notice/admin_add_notice.html')


# 增加公告逻辑（管理员）
def addlogic_notice(request):
    # 获取表单输入信息
    notice_id = request.POST.get('notice_id')
    admin = request.POST.get('admin')
    title = request.POST.get('title')
    #time = request.POST.get('time')
    #content = request.POST.get('content')
    print(notice_id, admin, title)
    TNotice.objects.create(notice_id=notice_id, admin_id=admin, title=title)
    return getdata_notice(request)


# 跳转修改公告页面（管理员）
def alter_notice(request):
    return render(request, 'notice/admin_alter_notice.html')


# 修改公告逻辑（管理员）
def alterlogic_class(request):
    return render(request, 'notice/admin_notice.html')


# 查看公告（学生）
def stu_notice(request):
    return render(request, 'notice/stu_notice.html')


# 查看公告（教师）
def teacher_notice(request):
    return render(request, 'notice/teacher_notice.html')
