from django.shortcuts import render
from loginapp.models import TEvaluation, TEvaluationDetail


# 转向教学评估管理信息页面（管理员）
def getdata_teach(request):
    teachlist = TEvaluation.objects.all()
    print(teachlist)
    return render(request, 'teach/admin_teach.html', {'list': teachlist})


# 跳转增加教学评估页面（管理员）
def add_teach(request):
    return render(request, 'teach/admin_add_teach.html')


# 增加教学评估（管理员）
def addlogic_teach(request):
    # 获取表单输入信息
    eval_id = request.POST.get('eval_id')
    class_id = request.POST.get('class_id')
    end_time = request.POST.get('end_time')
    teacher_id = request.POST.get('teacher_id')
    print(eval_id, class_id, teacher_id, end_time)
    TEvaluation.objects.create(evaluation_id=eval_id, class_id=class_id, teacher_id=teacher_id,
                               end_time=end_time)
    return getdata_teach(request)


# 跳转修改教学评估页面（管理员）
def alter_teach(request):
    return render(request, 'teach/admin_alter_teach.html')


# 修改教学评估逻辑（管理员）
def alterlogic_teach(request):
    return render(request, 'teach/admin_teach.html')


# 查看教学评估信息（学生）
def stu_teach(request):
    return render(request, 'teach/stu_teach.html')


# 填写/增加教学评估详情（学生）
def stu_teach_details(request):
    # 获取表单输入信息
    eval_id = request.POST.get('eval_id')
    stu_id = request.POST.get('stu_id')
    text1 = request.POST.get('text1')
    if text1 == 'perfect':
        text1 = 2
    if text1 == 'good':
        text1 = 1
    if text1 == 'bad':
        text1 = 0
    text2 = request.POST.get('text2')
    if text2 == 'perfect':
        text2 = 2
    if text2 == 'good':
        text2 = 1
    if text2 == 'bad':
        text2 = 0
    text3 = request.POST.get('text3')
    if text3 == 'perfect':
        text3 = 2
    if text3 == 'good':
        text3 = 1
    if text3 == 'bad':
        text3 = 0
    text4 = request.POST.get('text4')
    if text4 == 'perfect':
        text4 = 2
    if text4 == 'good':
        text4 = 1
    if text4 == 'bad':
        text4 = 0
    text5 = request.POST.get('text5')
    print(eval_id, stu_id, text1, text2, text3, text4, text5)
    TEvaluationDetail.objects.create(evaluation_id=eval_id, stu_id=stu_id, text1=text1, text2=text2,
                                     text13=text3, text4=text4, text5=text5)
    return render(request, 'teach/stu_teach_detail.html')


# 查看教学评估信息（教师）
def teacher_teach(request):
    return render(request, 'teach/teacher_teach.html')
