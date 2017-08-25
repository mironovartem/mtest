from django import forms
#from django.forms import ModelForm
#from egemath.models import UserAnswer

class TestAnswerForm(forms.Form):

    answer1 = forms.CharField(label='', max_length=30)
    answer2 = forms.CharField(label='', max_length=30)
    answer3 = forms.CharField(label='', max_length=30)
    answer4 = forms.CharField(label='', max_length=30)
    answer5 = forms.CharField(label='', max_length=30)
    answer6 = forms.CharField(label='', max_length=30)
    answer7 = forms.CharField(label='', max_length=30)
    answer8 = forms.CharField(label='', max_length=30)
    answer9 = forms.CharField(label='', max_length=30)
    answer10 = forms.CharField(label='', max_length=30)
    answer11 = forms.CharField(label='', max_length=30)
    answer12 = forms.CharField(label='', max_length=30)

class SignUpForm(forms.Form):
    #required_css_class = 'form-control'
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : '    Пароль'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : '    email'}))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : '    Пароль'}))

class CustomerApplicationForm(forms.Form):
    сontact_phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    номер телефона'}))
    сontact_email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : '    email'}))
    #сontact_details = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    номер телефона и/или email'}))
    сontact_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Ваше имя'}))
    location_samara = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    location_online = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    email_subscribe = forms.BooleanField(required=False, widget=forms.CheckboxInput(), initial=True)

class ContactsForm(forms.Form):
    сontact_details = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    номер телефона и/или email'}))
    сontact_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Ваше имя'}))
    сontact_question = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Ваш вопрос'}))
