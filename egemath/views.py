from django.shortcuts import render, render_to_response #
from django.shortcuts import redirect #
from django.http import HttpResponseRedirect #
from django.http import HttpResponse # для передачи ответото
from .forms import TestAnswerForm # импорт формы
from .forms import SignUpForm #импорт формы
from .models import EgeMathTest # импорт модели
from .models import UserAnswer # импорт модели
from django.contrib.auth.models import User, UserManager #нужно для регистрации пользователей
from django.contrib.auth import authenticate, login #нужно для аутентификации пользователей
from .forms import LoginForm #форма для авторизации
from django.contrib.auth import logout
from django.db.utils import IntegrityError #обработка исключения совпадения username при регистрации

# Create your views here.

def home_page(request):
    return render(request, 'egemath/home.html', {})

def about(request):
    return render(request, 'egemath/about.html', {})


def ege_math(request):
    return render(request, 'egemath/egemath.html', {})

'''
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
        #question_text_1 = question_text_1.get['question_text'] # так не работает почему?
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

'''

def egetest(request, test_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestAnswerForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            result = 0
            #username = request.user
            answer1 =  form.cleaned_data['answer1']
            answer2 =  form.cleaned_data['answer2']
            answer3 =  form.cleaned_data['answer3']
            answer4 =  form.cleaned_data['answer4']
            answer5 =  form.cleaned_data['answer5']
            answer6 =  form.cleaned_data['answer6']

            correct_answer = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 1).values('correct_answer')
            correct_answer = correct_answer[0]
            correct_answer1 = correct_answer['correct_answer']
            if correct_answer1 == answer1:
                result = result+1
                color1 = False
            else:
                color1 = True

            correct_answer = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 2).values('correct_answer')
            correct_answer = correct_answer[0]
            correct_answer2 = correct_answer['correct_answer']
            if correct_answer2 == answer2:
                result = result+1
                color2 = False
            else:
                color2 = True

            correct_answer = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 3).values('correct_answer')
            correct_answer = correct_answer[0]
            correct_answer3 = correct_answer['correct_answer']
            if correct_answer3 == answer3:
                result = result+1
                color3 = False
            else:
                color3 = True

            correct_answer = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 4).values('correct_answer')
            correct_answer = correct_answer[0]
            correct_answer4 = correct_answer['correct_answer']
            if correct_answer4 == answer4:
                result = result+1
                color4 = False
            else:
                color4 = True

            correct_answer = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 5).values('correct_answer')
            correct_answer = correct_answer[0]
            correct_answer5 = correct_answer['correct_answer']
            if correct_answer5 == answer5:
                result = result+1
                color5 = False
            else:
                color5 = True

            correct_answer = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 6).values('correct_answer')
            correct_answer = correct_answer[0]
            correct_answer6 = correct_answer['correct_answer']
            if correct_answer6 == answer6:
                result = result+1
                color6 = False
            else:
                color6 = True

            # redirect to a new URL:
            return render(request, 'egemath/egetestanswer.html', {
            #'test_id': 'test_id',
            'answer1': answer1,
            'correct_answer1' : correct_answer1,
            'color1': color1,

            'answer2': answer2,
            'correct_answer2' : correct_answer2,
            'color2': color2,

            'answer3': answer3,
            'correct_answer3' : correct_answer3,
            'color3': color3,

            'answer4': answer4,
            'correct_answer4' : correct_answer4,
            'color4': color4,

            'answer5': answer5,
            'correct_answer5' : correct_answer5,
            'color5': color5,

            'answer6': answer6,
            'correct_answer6' : correct_answer6,
            'color6': color6,

            'result': result
             })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestAnswerForm()

        question_text = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 1).values('question_text')
        #question_text_1 = question_text_1.get['question_text'] # так не работает почему?
        question_text = question_text[0]
        question_text_1 = question_text['question_text']

        question_image = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 1).values('question_image')
        question_image = question_image[0]
        question_image_1 = question_image['question_image']


        question_text = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 2).values('question_text')
        question_text = question_text[0]
        question_text_2 = question_text['question_text']

        question_image = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 2).values('question_image')
        question_image = question_image[0]
        question_image_2 = question_image['question_image']

        question_text = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 3).values('question_text')
        question_text = question_text[0]
        question_text_3 = question_text['question_text']

        question_image = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 3).values('question_image')
        question_image = question_image[0]
        question_image_3 = question_image['question_image']

        question_text = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 4).values('question_text')
        question_text = question_text[0]
        question_text_4 = question_text['question_text']

        question_image = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 4).values('question_image')
        question_image = question_image[0]
        question_image_4 = question_image['question_image']

        question_text = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 5).values('question_text')
        question_text = question_text[0]
        question_text_5 = question_text['question_text']

        question_image = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 5).values('question_image')
        question_image = question_image[0]
        question_image_5 = question_image['question_image']

        question_text = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 6).values('question_text')
        question_text = question_text[0]
        question_text_6 = question_text['question_text']

        question_image = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = 6).values('question_image')
        question_image = question_image[0]
        question_image_6 = question_image['question_image']

    return render(request, 'egemath/egetest.html', {
    'form': form,
    'question_text_1' : question_text_1,
    'question_image_1': question_image_1,

    'question_text_2' : question_text_2,
    'question_image_2': question_image_2,

    'question_text_3' : question_text_3,
    'question_image_3': question_image_3,

    'question_text_4' : question_text_4,
    'question_image_4': question_image_4,

    'question_text_5' : question_text_5,
    'question_image_5': question_image_5,

    'question_text_6' : question_text_6,
    'question_image_6': question_image_6,

    'test_id': test_id})

'''
def egetestanswer(request, test_id):
    username = request.user

    #answer_1 = UserAnswer.objects.filter(author__contains = username).filter(test_num__contains = test_id).filter(task_num__contains = 1).values('answer')
    #answer_1 = answer_1[0]
    #answer_1 = answer_1['answer']

    #answer_2 = UserAnswer.objects.filter(author__contains = username).filter(test_num__contains = test_id).filter(task_num__contains = 2).values('answer')
    #answer_2 = answer_2[0]
    #answer_2 = answer_2['answer']


    return render(request, 'egemath/egetestanswer.html', {
    #'test_id': 'test_id',
    'answer1': answer1,
    'correct_answer1' : correct_answer1,
    'color1': color1,
     'answer2': answer2,
    'correct_answer2' : correct_answer2,
    'color2': color2,
    'result': result
     })
'''


def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            password =  form.cleaned_data['password']
            email =  form.cleaned_data['email']
            username =  form.cleaned_data['username']

            if not User.objects.filter(email__contains = email): # пробуем получить уникальную почту на имя пользователя
                try:
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    if user is not None:
                        if user.is_active:
                            login(request, user)
                            return redirect('home_page')
                except  IntegrityError:
                    return render(request, 'registration/signup.html', {'form': form, 'username_not_uniq': True })
            else:
                return render(request, 'registration/signup.html', {'form': form, 'email_not_uniq': True })
            # redirect to a new URL:
            return redirect('login')
            #return HttpResponseRedirect('login')

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

        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect('home_page')
            #else:
                    # Return a 'disabled account' error message
                    #...
                #return render(request, 'registration/login.html', {'form': form, 'password_not_correct': True})
        else:
                # Return an 'invalid login' error message.
                #...
            return render(request, 'registration/login.html', {'form': form, 'password_not_correct': True})
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
