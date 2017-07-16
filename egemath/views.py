from django.shortcuts import render #
from django.shortcuts import redirect #
from django.http import HttpResponseRedirect #
from django.http import HttpResponse # для передачи ответотов типа
from .forms import TestAnswerForm # импорт формы
from .forms import SignUpForm #импорт формы
from .models import EgeMathTest # импорт модели
from .models import UserAnswer # импорт модели
from django.contrib.auth.models import User, UserManager #нужно для регистрации пользователей
from django.contrib.auth import authenticate, login #нужно для аутентификации пользователей
from .forms import LoginForm #форма для авторизации
from django.contrib.auth import logout

# Create your views here.

def home_page(request):
    return render(request, 'egemath/home.html', {})

def ege_math(request):
    return render(request, 'egemath/egemath.html', {})

def egetest(request, test_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestAnswerForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            username = request.user
            answer1 =  form.cleaned_data['answer1']
            answer2 =  form.cleaned_data['answer2']


            if UserAnswer.objects.filter(test_num__contains = test_id).filter(task_num__contains = 1).filter(author__contains = username):
                a1 = UserAnswer.objects.filter(test_num__contains = test_id).filter(task_num__contains = 1).filter(author__contains = username).get()
                a1.answer = answer1
                a1.save()
            else:
                a1 = UserAnswer( author = username, test_num = test_id, task_num = 1, answer = answer1)
                a1.save()


            if UserAnswer.objects.filter(test_num__contains = test_id).filter(task_num__contains = 2).filter(author__contains = username):
                a2 = UserAnswer.objects.filter(test_num__contains = test_id).filter(task_num__contains = 2).filter(author__contains = username).get()
                a2.answer = answer2
                a2.save()
            else:
                a2 = UserAnswer( author = username, test_num = test_id, task_num = 2, answer = answer2)
                a2.save()

            # redirect to a new URL:
            return HttpResponseRedirect('egetestanswer')
            #return render(request, 'egetestanswer', {'test_id':test_id})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestAnswerForm()

        question_text_1 = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 1).values('question_text')
        question_text_1 = question_text_1[0]
        question_text_1 = question_text_1['question_text']

        question_text_2 = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 2).values('question_text')
        question_text_2 = question_text_2[0]
        question_text_2 = question_text_2['question_text']

        question_image_2 = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 2).values('question_image')
        question_image_2 = question_image_2[0]
        question_image_2 = question_image_2['question_image']

    return render(request, 'egemath/egetest.html', {
    'form': form,
    'question_text_1' : question_text_1,
    'question_text_2' : question_text_2,
    'question_image_2': question_image_2,
    'test_id': test_id})


def egetestanswer(request, test_id):
    username = request.user

    answer_1 = UserAnswer.objects.filter(author__contains = username).filter(test_num__contains = test_id).filter(task_num__contains = 1).values('answer')
    answer_1 = answer_1[0]
    answer_1 = answer_1['answer']

    answer_2 = UserAnswer.objects.filter(author__contains = username).filter(test_num__contains = test_id).filter(task_num__contains = 2).values('answer')
    answer_2 = answer_2[0]
    answer_2 = answer_2['answer']


    return render(request, 'egemath/egetestanswer_1.html', {'answer_1' : answer_1 , 'answer_2' : answer_2})


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
            return HttpResponseRedirect('login')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()




    return render(request, 'registration/signup.html', {'form': form})

def log(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)


        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            username =  form.cleaned_data['username']
            password =  form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            #login(request, user)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect('home_page')
                #else:
                    # Return a 'disabled account' error message
                    #...
            #else:
                # Return an 'invalid login' error message.
                #...
            # redirect to a new URL:
            #return redirect('home_page')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()



    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home_page')
