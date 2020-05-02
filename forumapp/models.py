from django.db import models
from django.utils import timezone
# Create your models here.

class AdduserModel(models.Model):
    student='S'
    faculty='F'
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    USERTYPE = (
            (student, 'Student'),
            (faculty, 'Faculty'),
        )
    usertype = models.CharField(max_length=2,choices=USERTYPE, default=student,)


class AddQuestionsModel(models.Model):
    name = models.ForeignKey(AdduserModel, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)

class AddAnswersModel(models.Model):
    name=models.CharField(max_length=50)
    answer=models.TextField()
    question = models.ForeignKey(AddQuestionsModel, on_delete=models.CASCADE)

class CommentModel(models.Model):
    name=models.CharField(max_length=50)
    comment=models.TextField()
    commentfor=models.ForeignKey(AddAnswersModel, on_delete=models.CASCADE)
