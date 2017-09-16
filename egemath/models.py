from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class EgeMathTest(models.Model):
    """Модель таблицы с тестами егэ математика"""
    #author = models.CharField(max_length=30, blank=True, null=True)
    test_num = models.PositiveIntegerField()
    task_num = models.PositiveIntegerField()
    question_image = models.ImageField(upload_to='egetest', blank=True, null=True)
    question_text = models.TextField(blank=True, null=True)
    question_text1 = models.TextField(blank=True, null=True)
    question_text2 = models.TextField(blank=True, null=True)
    question_text3 = models.TextField(blank=True, null=True)
    #answer_text = models.TextField(blank=True, null=True)
    answer_text1 = models.TextField(blank=True, null=True)
    answer_text2 = models.TextField(blank=True, null=True)
    answer_text3 = models.TextField(blank=True, null=True)
    answer_text4 = models.TextField(blank=True, null=True)
    correct_answer = models.CharField(max_length=20)
    explanation_video = models.TextField(blank=True, null=True)
    access_level = models.PositiveIntegerField(blank=True, null=True)

    def publish(self):
        self.save()

class UserAccessLevel(models.Model):
    """Модель уровень доступа юзера к дополнительному контенту"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_access_level_ege = models.PositiveIntegerField(blank=True, null=True)



    def check_it(self):
        self.save()
