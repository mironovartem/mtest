from django.shortcuts import render, render_to_response #
from django.shortcuts import redirect #
from django.http import HttpResponseRedirect #
from django.http import HttpResponse # для передачи ответото
from .forms import TestAnswerForm # импорт формы
from .forms import SignUpForm #импорт формы
from .forms import CustomerApplicationForm #импорт формы
from .models import EgeMathTest # импорт модели
from .models import UserAnswer # импорт модели
from django.contrib.auth.models import User, UserManager #нужно для регистрации пользователей
from django.contrib.auth import authenticate, login #нужно для аутентификации пользователей
from .forms import LoginForm #форма для авторизации
from django.contrib.auth import logout
from django.db.utils import IntegrityError #обработка исключения совпадения username при регистрации
from django.core.mail import send_mail

# Create your views here.

def ege_math(request):
    return render(request, 'egemath/egemath.html', {})

def cor_answ(test_id, num):
    x = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('correct_answer')
    x = x[0]
    return  x['correct_answer']

def expl(test_id, num):
    x = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('explanation_text')
    x = x[0]
    x= x['explanation_text']
    if not x:
        x = ''
    y = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('explanation_video')
    y = y[0]
    y = y['explanation_video']
    if y:
        x = ''
    return  x, y

def quest(test_id, num):
    x= EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('question_text')
    x = x[0]
    x = x['question_text']

    y = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('question_image')
    y = y[0]
    y = y['question_image']
    return  x, y

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
            answer7 =  form.cleaned_data['answer7']
            answer8 =  form.cleaned_data['answer8']
            answer9 =  form.cleaned_data['answer9']
            answer10 =  form.cleaned_data['answer10']

###############################
            correct_answer1 = cor_answ(test_id, 1)
            explanation_text1, explanation_video1 =expl(test_id, 1)

            if correct_answer1 == answer1:
                result = result+1
                color1 = False
            else:
                color1 = True
###################################
            correct_answer2 = cor_answ(test_id, 2)
            explanation_text2, explanation_video2 =expl(test_id, 2)

            if correct_answer2 == answer2:
                result = result+1
                color2 = False
            else:
                color2 = True
#####################################
            correct_answer3 = cor_answ(test_id, 3)
            explanation_text3, explanation_video3 =expl(test_id, 3)

            if correct_answer3 == answer3:
                result = result+1
                color3 = False
            else:
                color3 = True
######################################
            correct_answer4 = cor_answ(test_id, 4)
            explanation_text4, explanation_video4 =expl(test_id, 4)

            if correct_answer4 == answer4:
                result = result+1
                color4 = False
            else:
                color4 = True
#######################################
            correct_answer5 = cor_answ(test_id, 5)
            explanation_text5, explanation_video5 =expl(test_id, 5)

            if correct_answer5 == answer5:
                result = result+1
                color5 = False
            else:
                color5 = True
#########################################
            correct_answer6 = cor_answ(test_id, 6)
            explanation_text6, explanation_video6 =expl(test_id, 6)

            if correct_answer6 == answer6:
                result = result+1
                color6 = False
            else:
                color6 = True
##########################################
            correct_answer7 = cor_answ(test_id, 7)
            explanation_text7, explanation_video7 =expl(test_id, 7)

            if correct_answer7 == answer7:
                result = result+1
                color7 = False
            else:
                color7 = True
##########################################
            correct_answer8 = cor_answ(test_id, 8)
            explanation_text8, explanation_video8 =expl(test_id, 8)

            if correct_answer8 == answer8:
                result = result+1
                color8 = False
            else:
                color8 = True
##########################################
            correct_answer9 = cor_answ(test_id, 9)
            explanation_text9, explanation_video9 =expl(test_id, 9)

            if correct_answer9 == answer9:
                result = result+1
                color9 = False
            else:
                color9 = True
##########################################
            correct_answer10 = cor_answ(test_id, 10)
            explanation_text10, explanation_video10 =expl(test_id, 10)

            if correct_answer10 == answer10:
                result = result+1
                color10 = False
            else:
                color10 = True
##########################################
            # redirect to a new URL:
            return render(request, 'egemath/egetestanswer.html', {
            #'test_id': 'test_id',
            'answer1': answer1,
            'correct_answer1' : correct_answer1,
            'color1' : color1,
            'explanation_text1' : explanation_text1,
            'explanation_video1' : explanation_video1,

            'answer2' : answer2,
            'correct_answer2' : correct_answer2,
            'color2': color2,
            'explanation_text2' : explanation_text2,
            'explanation_video2' : explanation_video2,

            'answer3': answer3,
            'correct_answer3' : correct_answer3,
            'color3': color3,
            'explanation_text3' : explanation_text3,
            'explanation_video3' : explanation_video3,

            'answer4': answer4,
            'correct_answer4' : correct_answer4,
            'color4': color4,
            'explanation_text4' : explanation_text4,
            'explanation_video4' : explanation_video4,

            'answer5': answer5,
            'correct_answer5' : correct_answer5,
            'color5': color5,
            'explanation_text5' : explanation_text5,
            'explanation_video5' : explanation_video5,

            'answer6': answer6,
            'correct_answer6' : correct_answer6,
            'color6': color6,
            'explanation_text6' : explanation_text6,
            'explanation_video6' : explanation_video6,

            'answer7': answer7,
            'correct_answer7' : correct_answer7,
            'color7': color7,
            'explanation_text7' : explanation_text7,
            'explanation_video7' : explanation_video7,

            'answer8': answer8,
            'correct_answer8' : correct_answer8,
            'color8': color8,
            'explanation_text8' : explanation_text8,
            'explanation_video8' : explanation_video8,

            'answer9': answer9,
            'correct_answer9' : correct_answer9,
            'color9': color9,
            'explanation_text9' : explanation_text9,
            'explanation_video9' : explanation_video9,

            'answer10': answer10,
            'correct_answer10' : correct_answer10,
            'color10': color10,
            'explanation_text10' : explanation_text10,
            'explanation_video10' : explanation_video10,

            'result': result
             })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestAnswerForm()
#################################
        question_text_1, question_image_1 = quest(test_id, 1)
        question_text_2, question_image_2 = quest(test_id, 2)
        question_text_3, question_image_3 = quest(test_id, 3)
        question_text_4, question_image_4 = quest(test_id, 4)
        question_text_5, question_image_5 = quest(test_id, 5)
        question_text_6, question_image_6 = quest(test_id, 6)
        question_text_7, question_image_7 = quest(test_id, 7)
        question_text_8, question_image_8 = quest(test_id, 8)
        question_text_9, question_image_9 = quest(test_id, 9)
        question_text_10, question_image_10 = quest(test_id, 10)

#####################################
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

    'question_text_7' : question_text_7,
    'question_image_7': question_image_7,

    'question_text_8' : question_text_8,
    'question_image_8': question_image_8,

    'question_text_9' : question_text_9,
    'question_image_9': question_image_9,

    'question_text_10' : question_text_10,
    'question_image_10': question_image_10,

    'test_id': test_id})

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
                            return redirect('donate')
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

def home_page(request):
    return render(request, 'egemath/home.html', {})

def about(request):
    return render(request, 'egemath/about.html', {})
def about_me(request):
    return render(request, 'egemath/about_me.html', {})

def repetitor_math(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = CustomerApplicationForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...

                message =  form.cleaned_data['сontact_details']
                сontact_name =  form.cleaned_data['сontact_name']
                location_samara =  form.cleaned_data['location_samara']
                location_online =  form.cleaned_data['location_online']


                if message:
                    #send_mail('application', message, 'admin@testege.com', ['astruslux@gmail.com'])
                    send_mail('Заявка на консультацию', 'Контактные данные:  ' + message +', '+ 'Имя: '+ сontact_name+','+' Самара: ' + str(location_samara) + ', '+' Online: ' + str(location_online), 'astruslux@gmail.com', ['creativerror@gmail.com'] )


                # redirect to a new URL:
                return HttpResponseRedirect('thanks')


        # if a GET (or any other method) we'll create a blank form
        else:
            form = CustomerApplicationForm()

        return render(request, 'egemath/repetitor_math.html', {'form': form})


def donate(request):
    return render(request, 'egemath/donate.html', {})

def copyright(request):
    return render(request, 'egemath/copyright.html', {})

def advertising(request):
    return render(request, 'egemath/advertising.html', {})

def website_development(request):
    return render(request, 'egemath/website_development.html', {})

def contacts(request):
    return render(request, 'egemath/contacts.html', {})

def thanks(request):
    return render(request, 'egemath/thanks.html', {})

def egetaskanswer(request):
    return render(request, 'egemath/egetaskanswer.html', {})

def egetask(request):
    return render(request, 'egemath/egetask.html', {})
