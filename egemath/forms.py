from django import forms
#from django.forms import ModelForm
#from egemath.models import UserAnswer

class TestAnswerForm(forms.Form):

    answer1 = forms.CharField(label='', max_length=30)
    answer2 = forms.CharField(label='', max_length=30)
    #answer3 = forms.CharField(label='', max_length=30)
    #answer4 = forms.CharField(label='', max_length=30)
    #answer5 = forms.CharField(label='', max_length=30)
    #answer6 = forms.CharField(label='', max_length=30)
    #answer7 = forms.CharField(label='', max_length=30)
    #answer8 = forms.CharField(label='', max_length=30)
    #answer9 = forms.CharField(label='', max_length=30)
    #answer10 = forms.CharField(label='', max_length=30)
    #answer11 = forms.CharField(label='', max_length=30)
    #answer12 = forms.CharField(label='', max_length=30)

class SignUpForm(forms.Form):
    username = forms.CharField(label='', help_text = 'Имя пользователя')

    password = forms.CharField(label='', widget=forms.PasswordInput, help_text="Пароль")
    email = forms.EmailField()
