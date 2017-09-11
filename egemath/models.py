from django.db import models
from django.utils import timezone

# Create your models here.


class UserAnswer(models.Model):
    """Модель описывает таблицу в которой сохраняются значения
    ответов на стандартный тест егэ по математике,
    введеные авторизованным или нет пользователем"""
    author = models.CharField(max_length=30)
    test_num=models.PositiveIntegerField()
    task_num = models.PositiveIntegerField()
    answer= models.CharField(max_length=20, blank=True, null=True)

    def check_it(self):
        self.save()

    #def __str__(self):
        #return self.title

class EgeMathTest(models.Model):
    """Модель таблицы с тестами егэ математика"""
    #author = models.CharField(max_length=30, blank=True, null=True)
    test_num=models.PositiveIntegerField()
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
    explanation_text = models.TextField(blank=True, null=True)
    access_level = models.TextField(blank=True, null=True)

    def publish(self):
        self.save()
