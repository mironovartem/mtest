from django.shortcuts import render #
from django.http import HttpResponseRedirect #
from django.http import HttpResponse # для передачи ответотов типа
from .forms import TestAnswerForm # импорт формы
from .forms import SignUpForm #импорт формы
from .models import EgeMathTest # импорт модели
from .models import UserAnswer # импорт модели
from django.contrib.auth.models import User #нужно для регистрации пользователей
from django.contrib.auth import authenticate #нужно для аутентификации пользователей
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home_page(request):
    return render(request, 'egemath/home.html', {})

def ege_math(request):
    return render(request, 'egemath/egemath.html', {})

def egetest_1(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestAnswerForm(request.POST)
        #question_text_1 = EgeMathTest.objects.filter(test_num__contains = 1).filter(task_num__contains = 1).values('question_text')
        #question_text_1 = question_text_1[0]
        #question_text_1 = question_text_1['question_text']

        #question_text_2 = EgeMathTest.objects.filter(test_num__contains = 1).filter(task_num__contains = 2).values('question_text')
        #question_text_2 = question_text_2[0]
        #question_text_2 = question_text_2['question_text']

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            answer1 =  form.cleaned_data['answer1']

            if UserAnswer.objects.filter(test_num__contains = 1).filter(task_num__contains = 1):
                a1 = UserAnswer.objects.filter(test_num__contains = 1).filter(task_num__contains = 1).get()
                a1.answer = answer1
                a1.save()
            else:
                a1 = UserAnswer( author = 'ara', test_num = 1, task_num = 1, answer = answer1)
                a1.save()

            # redirect to a new URL:
            return HttpResponseRedirect('egetestanswer_1.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestAnswerForm()
        #form2 = TestAnswerForm2()

        question_text_1 = EgeMathTest.objects.filter(test_num__contains = 1).filter(task_num__contains = 1).values('question_text')
        question_text_1 = question_text_1[0]
        question_text_1 = question_text_1['question_text']

        question_text_2 = EgeMathTest.objects.filter(test_num__contains = 1).filter(task_num__contains = 2).values('question_text')
        question_text_2 = question_text_2[0]
        question_text_2 = question_text_2['question_text']


    return render(request, 'egemath/egetest_1.html', {
    'form': form,
    #'form2': form2,
    'question_text_1' : question_text_1 ,
    'question_text_2' : question_text_2})

def egetest(request, test_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestAnswerForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            answer1 =  form.cleaned_data['answer1']

            if UserAnswer.objects.filter(test_num__contains = test_id).filter(task_num__contains = 1):
                a1 = UserAnswer.objects.filter(test_num__contains = test_id).filter(task_num__contains = 1).get()
                a1.answer = answer1
                a1.save()
            else:
                a1 = UserAnswer( author = 'art', test_num = test_id, task_num = 1, answer = answer1)
                a1.save()

            # redirect to a new URL:
            return HttpResponseRedirect('egetestanswer')
            #return render(request, 'egetestanswer', {'test_id':test_id})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestAnswerForm()
        #form2 = TestAnswerForm2()

        question_text_1 = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 1).values('question_text')
        question_text_1 = question_text_1[0]
        question_text_1 = question_text_1['question_text']

        question_text_2 = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 2).values('question_text')
        question_text_2 = question_text_2[0]
        question_text_2 = question_text_2['question_text']


    return render(request, 'egemath/egetest.html', {
    'form': form,
    #'form2': form2,
    'question_text_1' : question_text_1 ,
    'question_text_2' : question_text_2,
    'test_id': test_id})


def egetestanswer(request, test_id):
    answer_1_1 = UserAnswer.objects.filter(author__contains = 'art').filter(test_num__contains = test_id).filter(task_num__contains = 1).values('answer')
    answer_1_1 = answer_1_1[0]
    answer_1_1 = answer_1_1['answer']


    return render(request, 'egemath/egetestanswer_1.html', {'answer_1_1' : answer_1_1 , 'answer_1_2' : 2})


def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)


        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            username =  form.cleaned_data['username']
            password =  form.cleaned_data['password']
            email =  form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.save()



            # redirect to a new URL:
            return HttpResponseRedirect('login.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()




    return render(request, 'registration/signup.html', {'form': form})

def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(request.POST)


        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            username =  form.cleaned_data['username']
            password =  form.cleaned_data['password']
            user = authenticate(username=username, password=password)





            # redirect to a new URL:
            return render(request, 'home.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()



    return render(request, 'registration/login.html', {'form': form})
