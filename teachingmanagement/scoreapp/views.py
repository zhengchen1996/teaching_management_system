from django.shortcuts import render

# Create your views here.
from loginapp.models import TScore


# 转向查询个人成绩页面（学生）
def stu_score(request):
    return render(request, 'score/stu_score.html')


# 转向学生成绩管理页面（教师）
def getdata_score(request):
    scorelist = TScore.objects.all()
    print(scorelist)
    return render(request, 'score/teacher_score.html', {'list': scorelist})


# 转向打分页面
def add_score(request):
    return render(request, 'score/teacher_mark.html')


# 增加学生成绩（教师）
def addlogic_score(request):
    # 获取表单输入信息
    stu_id = request.POST.get('stu_id')
    grade = request.POST.get('grade')
    print(stu_id, grade)
    TScore.objects.create(stu_id=stu_id, grade=grade)
    return getdata_score(request)


