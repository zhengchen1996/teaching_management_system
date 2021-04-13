from django.db import models


# Create your models here.
class TStu(models.Model):  # 学生
    stu_id = models.IntegerField(primary_key=True)  # 学号
    password = models.CharField(max_length=50, blank=True, null=True)     # 密码
    name = models.CharField(max_length=50, blank=True, null=True)         # 姓名
    sex = models.CharField(max_length=10, blank=True, null=True)          # 性别
    native = models.CharField(max_length=50, blank=True, null=True)       # 籍贯
    birthday = models.DateField(blank=True, null=True)     # 出生日期
    entrance = models.DateField(blank=True, null=True)      # 入学日期
    academy = models.CharField(max_length=50, blank=True, null=True)      # 学院
    major = models.CharField(max_length=50, blank=True, null=True)        # 专业
    sclass = models.CharField(max_length=50, blank=True, null=True)       # 班级
    telephone = models.CharField(max_length=50, blank=True, null=True)    # 联系电话

    class Meta:
        db_table = 't_stu'


class TTeacher(models.Model):  # 教师
    teacher_id = models.IntegerField(primary_key=True)  # 教师工号
    password = models.CharField(max_length=50, blank=True, null=True)  # 密码
    name = models.CharField(max_length=50, blank=True, null=True)  # 姓名
    sex = models.CharField(max_length=10, blank=True, null=True)  # 性别
    native = models.CharField(max_length=50, blank=True, null=True)  # 籍贯
    birthday = models.DateField(blank=True, null=True)  # 出生日期
    diplomas = models.CharField(max_length=20, blank=True, null=True)  # 学历
    politics = models.CharField(max_length=20, blank=True, null=True)  # 政治面貌
    entrance = models.DateField(blank=True, null=True)  # 入职年份
    job_title = models.CharField(max_length=20, blank=True, null=True)  # 职称
    academy = models.CharField(max_length=50, blank=True, null=True)  # 学院
    telephone = models.CharField(max_length=50, blank=True, null=True)  # 联系电话

    class Meta:
        db_table = 't_teacher'


class TAdmin(models.Model):  # 管理员
    admin_id = models.IntegerField(primary_key=True)  # 工号
    password = models.CharField(max_length=50, blank=True, null=True)  # 密码
    name = models.CharField(max_length=50, blank=True, null=True)  # 姓名
    sex = models.CharField(max_length=10, blank=True, null=True)  # 性别
    telephone = models.CharField(max_length=50, blank=True, null=True)  # 联系电话

    class Meta:
        db_table = 't_admin'


class TClass(models.Model):  # 课程表
    class_id = models.IntegerField(primary_key=True)  # 课程号
    name = models.CharField(max_length=50, blank=True, null=True)   # 课程名称
    teacher_id = models.ForeignKey(TTeacher, models.DO_NOTHING, blank=True, null=True)  # 授课教师工号
    #book = models.ForeignKey(TBookDetails, models.DO_NOTHING, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)                # 节数 第几节上课 1~5
    week = models.IntegerField(blank=True, null=True)               # 周几上课 1~7
    place = models.CharField(max_length=50, blank=True, null=True)   # 上课地点
    category = models.CharField(max_length=20, blank=True, null=True)  # 课程类别
    academy = models.CharField(max_length=50, blank=True, null=True)  # 所属院系
    credit = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)    # 学分

    class Meta:
        db_table = 't_class'


# 已选课程表
class TClassSelected(models.Model):
    class_id = models.ForeignKey(TClass, models.DO_NOTHING, blank=True, null=True)  # 课程代码
    stu_id = models.ForeignKey(TStu, models.DO_NOTHING, blank=True, null=True)  # 学生学号

    class Meta:
        db_table = 't_class_selected'


class TNotice(models.Model):  # 通知公告
    notice_id = models.IntegerField(primary_key=True)  # 公告编号
    admin_id = models.ForeignKey(TAdmin, models.DO_NOTHING, blank=True, null=True)   # 发布人
    title = models.CharField(max_length=50, blank=True, null=True)     # 标题
    content = models.CharField(max_length=1000, blank=True, null=True)  # 内容
    publish_time = models.DateField(blank=True, null=True)  # 发布日期

    class Meta:
        db_table = 't_notice'


class TScore(models.Model):  # 成绩表
    score_id = models.IntegerField(primary_key=True)  # 成绩id
    class_id = models.ForeignKey(TClass, models.DO_NOTHING, blank=True, null=True)  # 课程代码
    stu_id = models.ForeignKey(TStu, models.DO_NOTHING, blank=True, null=True)  # 学生学号
    grade = models.IntegerField(blank=True, null=True)  # 成绩

    class Meta:
        db_table = 't_score'


class TExam(models.Model):  # 考务表
    exam_id = models.IntegerField(primary_key=True)  # 考务编号
    class_id = models.ForeignKey(TClass, models.DO_NOTHING, blank=True, null=True)  # 课程代码
    time = models.CharField(max_length=50, blank=True, null=True)  # 考试时间
    place = models.CharField(max_length=50, blank=True, null=True)  # 考试地点
    teacher_id = models.ForeignKey(TTeacher, models.DO_NOTHING, blank=True, null=True)  # 监考人

    class Meta:
        db_table = 't_exam'


class TGradeExam(models.Model):  # 等级考试表
    grade_id = models.IntegerField(primary_key=True)  # 等级考试编号
    name = models.CharField(max_length=30, blank=True, null=True)  # 考试名称
    exam_time = models.DateField(blank=True, null=True)  # 考试日期
    end_time = models.DateField(blank=True, null=True)  # 报考截止时间

    class Meta:
        db_table = 't_gradeexam'


# 已报名等级考试表
class TGradeSigned(models.Model):
    grade_id = models.ForeignKey(TGradeExam, models.DO_NOTHING, blank=True, null=True)  # 等级考试编号
    stu_id = models.ForeignKey(TStu, models.DO_NOTHING, blank=True, null=True)  # 学生学号

    class Meta:
        db_table = 't_grade_signed'


class TEvaluation(models.Model):  # 教学评估表
    eval_id = models.IntegerField(primary_key=True)  # 教学评估编号
    class_id = models.ForeignKey(TClass, models.DO_NOTHING, blank=True, null=True)  # 课程号
    teacher_id = models.ForeignKey(TTeacher, models.DO_NOTHING, blank=True, null=True)  # 任课教师编号
    end_time = models.DateField(blank=True, null=True)  # 填写截止时间

    class Meta:
        db_table = 't_evaluation'


# 教学评估详情表
class TEvaluationDetail(models.Model):
    eval_id = models.ForeignKey(TEvaluation, models.DO_NOTHING, blank=True, null=True)  # 教学评估编号
    stu_id = models.ForeignKey(TStu, models.DO_NOTHING, blank=True, null=True)  # 学生学号
    text1 = models.IntegerField(blank=True, null=True)  # 问题一得分
    text2 = models.IntegerField(blank=True, null=True)  # 问题二得分
    text3 = models.IntegerField(blank=True, null=True)  # 问题三得分
    text4 = models.IntegerField(blank=True, null=True)  # 问题四得分
    text5 = models.CharField(max_length=50, blank=True, null=True)  # 问题五详情

    class Meta:
        db_table = 't_evaluation_detail'
