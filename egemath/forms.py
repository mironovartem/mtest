from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput
from egemath.models import EgeMathTest

class TestAnswerForm(forms.Form):

    answer1 = forms.CharField(required=False, label='', max_length=30)
    answer2 = forms.CharField(required=False, label='', max_length=30)
    answer3 = forms.CharField(required=False, label='', max_length=30)
    answer4 = forms.CharField(required=False, label='', max_length=30)
    answer5 = forms.CharField(required=False, label='', max_length=30)
    answer6 = forms.CharField(required=False, label='', max_length=30)
    answer7 = forms.CharField(required=False, label='', max_length=30)
    answer8 = forms.CharField(required=False, label='', max_length=30)
    answer9 = forms.CharField(required=False, label='', max_length=30)
    answer10 = forms.CharField(required=False, label='', max_length=30)
    answer11 = forms.CharField(required=False, label='', max_length=30)
    answer12 = forms.CharField(required=False, label='', max_length=30)
    answer13 = forms.CharField(required=False, label='', max_length=30)
    answer14 = forms.CharField(required=False, label='', max_length=30)
    answer15 = forms.CharField(required=False, label='', max_length=30)
    answer16 = forms.CharField(required=False, label='', max_length=30)
    answer17 = forms.CharField(required=False, label='', max_length=30)
    answer18 = forms.CharField(required=False, label='', max_length=30)
    answer19 = forms.CharField(required=False, label='', max_length=30)

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : '    Пароль'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : '    email'}))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : '    Пароль'}))

class CustomerApplicationForm(forms.Form):
    сontact_phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    номер телефона'}))
    сontact_email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : '    email (если есть)'}))
    сontact_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Ваше имя'}))
    location_samara = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    location_online = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    email_subscribe = forms.BooleanField(required=False, widget=forms.CheckboxInput(), initial=True)
    offer_accepted = forms.BooleanField(required=False, widget=forms.CheckboxInput(), initial=True)

class EgeTestInputForm(ModelForm):

    class Meta:
        model = EgeMathTest
        fields = [
        'test_num', 'task_num', 'question_image', 'question_text',
        'question_text1', 'question_text2', 'question_text3', 'answer_text1',
        'answer_text2', 'answer_text3', 'answer_text4', 'correct_answer',
        'explanation_video', 'access_level',]
        widgets = {
        #'test_num': IntegerField(attrs={'class' : 'form-control', 'placeholder' : '     Номер теста test_num'}),
        #'task_num': IntegerField(attrs={'class' : 'form-control', 'placeholder' : '     Номер задания task_num'}),
        #'question_image': ImageField(attrs={'class' : 'form-control', 'placeholder' : '     question_text1'}),
        'question_text': Textarea(attrs={'rows': 6, 'class' : 'form-control', 'placeholder' : '     question_text'}),
        'question_text1': Textarea(attrs={'rows': 3, 'class' : 'form-control', 'placeholder' : '    question_text1'}),
        'question_text2': Textarea(attrs={'rows': 3, 'class' : 'form-control', 'placeholder' : '    question_text2'}),
        'question_text3': Textarea(attrs={'rows': 3, 'class' : 'form-control', 'placeholder' : '    question_text3'}),
        'answer_text1': Textarea(attrs={'rows': 3, 'class' : 'form-control', 'placeholder' : '  1 Вариант ответа answer_text1'}),
        'answer_text2': Textarea(attrs={'rows': 3, 'class' : 'form-control', 'placeholder' : '  2 Вариант ответа answer_text2'}),
        'answer_text3': Textarea(attrs={'rows': 3, 'class' : 'form-control', 'placeholder' : '  3 Вариант ответа answer_text3'}),
        'answer_text4': Textarea(attrs={'rows': 3, 'class' : 'form-control', 'placeholder' : '  4 Вариант ответа answer_text4'}),
        'correct_answer': TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Правильный ответ correct_answer'}),
        'explanation_video': TextInput(attrs={'class' : 'form-control', 'placeholder' : '   Видео с объяснением explanation_video'}),
        'access_level': NumberInput(attrs={'class' : 'form-control', 'placeholder' : '    Уровень доступа access_level'}),
        }

class AdmistratorForm(forms.Form):
    test_num = forms.IntegerField(widget = forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : '    Номер теста егэ'}))
    task_num = forms.IntegerField(widget = forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : '    Номер задания'}))
