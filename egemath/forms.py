from django import forms

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

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : '    Пароль'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : '    email'}))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : '    Пароль'}))

class CustomerApplicationForm(forms.Form):
    сontact_phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    номер телефона'}))
    сontact_email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : '    email'}))
    сontact_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Ваше имя'}))
    location_samara = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    location_online = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    email_subscribe = forms.BooleanField(required=False, widget=forms.CheckboxInput(), initial=True)

class ContactsForm(forms.Form):
    сontact_details = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    номер телефона и/или email'}))
    сontact_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Ваше имя'}))
    сontact_question = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '    Ваш вопрос'}))
