from .forms import AdmistratorForm #импорт формы
from .forms import CustomerApplicationForm #импорт формы
from .forms import EgeTestInputForm #импорт формы
from .forms import LoginForm #форма для авторизации
from .forms import SignUpForm #импорт формы
from .forms import TestAnswerForm # импорт формы
from .models import EgeMathTest # импорт модели
from .models import UserAccessLevel # импорт модели
from django.contrib.auth import authenticate, login #нужно для аутентификации пользователей
from django.contrib.auth import logout
from django.contrib.auth.models import User, UserManager #нужно для регистрации пользователей
from django.core.files.uploadedfile import SimpleUploadedFile # нужно для загрузки изображений
from django.core.mail import send_mail
from django.db.utils import IntegrityError #обработка исключения совпадения username при регистрации
from django.forms import ModelForm
from django.http import Http404
from django.http import HttpResponse, HttpResponseServerError # для передачи ответото
from django.http import HttpResponseRedirect #
from django.shortcuts import get_object_or_404, render, render_to_response #
from django.shortcuts import redirect #
from local_settings import GOOGLE_RECAPTCHA_SECRET_KEY
from urllib import request
import json
import urllib
#from django.contrib import messages



# Create your views here.


def ege_math(request):
    #username = request.user

    return render(request, 'egemath/egemath.html') #, {'username': username}

def cor_answ(test_id, num): # находит правильный ответ
    x = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('correct_answer')
    #x = get_object_or_404(EgeMathTest, test_num = test_id)  .objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('correct_answer')
    x = x[0]
    return  x['correct_answer']

def expl(test_id, num):
    try:
        x = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('access_level')
        x = x[0]
        x= x['access_level']
    except:
        x = 0
    if x == None:
        x =0
    y = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('explanation_video')
    y = y[0]
    y = y['explanation_video']

    return  x, y

def quest(test_id, num):
    if num >=13:
        x= EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('question_text')
        #x = get_object_or_404(EgeMathTest, test_num = test_id, task_num = num).question_text
        x = x[0]
        x = x['question_text']

        x1= EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('question_text1')
        x1 = x1[0]
        x1 = x1['question_text1']
        if not x1:
            x1 = ''

        x2= EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('question_text2')
        x2 = x2[0]
        x2 = x2['question_text2']
        if not x2:
            x2 = ''

        x3= EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('question_text3')
        x3 = x3[0]
        x3 = x3['question_text3']
        if not x3:
            x3 = ''

        y = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('question_image')
        y = y[0]
        y = y['question_image']
        return  x, y, x1, x2, x3
    else:
        x= EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('question_text')
        x = x[0]
        x = x['question_text']

        y = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('question_image')
        y = y[0]
        y = y['question_image']
        return  x, y

def aswertext(test_id, num):
    x1 = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('answer_text1')
    x1 = x1[0]
    x1 = x1['answer_text1']

    x2 = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('answer_text2')
    x2 = x2[0]
    x2 = x2['answer_text2']

    x3 = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('answer_text3')
    x3 = x3[0]
    x3 = x3['answer_text3']

    x4 = EgeMathTest.objects.filter(test_num__contains = test_id).filter(task_num__contains = num).values('answer_text4')
    x4 = x4[0]
    x4 = x4['answer_text4']
    return x1, x2, x3, x4


def egetest(request, test_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestAnswerForm(request.POST)

        username = request.user #определение уровня доступа пользователя
        if request.user.is_authenticated():
            #user_access_level_ege = User.objects.filter(username__contains = username).values('useraccesslevel').first()
            try:
                user_access_level_ege = UserAccessLevel.objects.filter(user = username).values('user_access_level_ege').first()
            #user_access_level_ege = UserAccessLevel.objects.filter(user = username).values('user_access_level_ege').first()
                user_access_level_ege = user_access_level_ege['user_access_level_ege']
            except:
                user_access_level_ege = 0
            if user_access_level_ege == None:
                user_access_level_ege = 0


        else:
            user_access_level_ege = 0

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            result = 0
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
            answer11 =  form.cleaned_data['answer11']
            answer12 =  form.cleaned_data['answer12']
            answer13 =  form.cleaned_data['answer13']
            answer14 =  form.cleaned_data['answer14']
            answer15 =  form.cleaned_data['answer15']
            answer16 =  form.cleaned_data['answer16']
            answer17 =  form.cleaned_data['answer17']
            answer18 =  form.cleaned_data['answer18']
            answer19 =  form.cleaned_data['answer19']

###############################
            correct_answer1 = cor_answ(test_id, 1)
            access_level1, explanation_video1 =expl(test_id, 1)

            if correct_answer1 == answer1:
                result = result+1
                color1 = False
            else:
                color1 = True
###################################
            correct_answer2 = cor_answ(test_id, 2)
            access_level2, explanation_video2 =expl(test_id, 2)

            if correct_answer2 == answer2:
                result = result+1
                color2 = False
            else:
                color2 = True
#####################################
            correct_answer3 = cor_answ(test_id, 3)
            access_level3, explanation_video3 =expl(test_id, 3)

            if correct_answer3 == answer3:
                result = result+1
                color3 = False
            else:
                color3 = True
######################################
            correct_answer4 = cor_answ(test_id, 4)
            access_level4, explanation_video4 =expl(test_id, 4)

            if correct_answer4 == answer4:
                result = result+1
                color4 = False
            else:
                color4 = True
#######################################
            correct_answer5 = cor_answ(test_id, 5)
            access_level5, explanation_video5 =expl(test_id, 5)

            if correct_answer5 == answer5:
                result = result+1
                color5 = False
            else:
                color5 = True
#########################################
            correct_answer6 = cor_answ(test_id, 6)
            access_level6, explanation_video6 =expl(test_id, 6)

            if correct_answer6 == answer6:
                result = result+1
                color6 = False
            else:
                color6 = True
##########################################
            correct_answer7 = cor_answ(test_id, 7)
            access_level7, explanation_video7 =expl(test_id, 7)

            if correct_answer7 == answer7:
                result = result+1
                color7 = False
            else:
                color7 = True
##########################################
            correct_answer8 = cor_answ(test_id, 8)
            access_level8, explanation_video8 =expl(test_id, 8)

            if correct_answer8 == answer8:
                result = result+1
                color8 = False
            else:
                color8 = True
##########################################
            correct_answer9 = cor_answ(test_id, 9)
            access_level9, explanation_video9 =expl(test_id, 9)

            if correct_answer9 == answer9:
                result = result+1
                color9 = False
            else:
                color9 = True
##########################################
            correct_answer10 = cor_answ(test_id, 10)
            access_level10, explanation_video10 =expl(test_id, 10)

            if correct_answer10 == answer10:
                result = result+1
                color10 = False
            else:
                color10 = True
##########################################
            correct_answer11 = cor_answ(test_id, 11)
            access_level11, explanation_video11 =expl(test_id, 11)

            if correct_answer11 == answer11:
                result = result+1
                color11 = False
            else:
                color11 = True
##########################################
            correct_answer12 = cor_answ(test_id, 12)
            access_level12, explanation_video12 =expl(test_id, 12)

            if correct_answer12 == answer12:
                result = result+1
                color12 = False
            else:
                color12 = True
##########################################
            correct_answer13 = cor_answ(test_id, 13)
            access_level13, explanation_video13 =expl(test_id, 13)

            if correct_answer13 == answer13:
                result = result+1
                color13 = False
            else:
                color13 = True
##########################################
            correct_answer14 = cor_answ(test_id, 14)
            access_level14, explanation_video14 =expl(test_id, 14)

            if correct_answer14 == answer14:
                result = result+1
                color14 = False
            else:
                color14 = True
##########################################
            correct_answer15 = cor_answ(test_id, 15)
            access_level15, explanation_video15 =expl(test_id, 15)

            if correct_answer15 == answer15:
                result = result+1
                color15 = False
            else:
                color15 = True
##########################################
            correct_answer16 = cor_answ(test_id, 16)
            access_level16, explanation_video16 =expl(test_id, 16)

            if correct_answer16 == answer16:
                result = result+1
                color16 = False
            else:
                color16 = True
##########################################
            correct_answer17 = cor_answ(test_id, 17)
            access_level17, explanation_video17 =expl(test_id, 17)

            if correct_answer17 == answer17:
                result = result+1
                color17 = False
            else:
                color17 = True
##########################################
            correct_answer18 = cor_answ(test_id, 18)
            access_level18, explanation_video18 =expl(test_id, 18)

            if correct_answer18 == answer18:
                result = result+1
                color18 = False
            else:
                color18 = True
##########################################
            correct_answer19 = cor_answ(test_id, 19)
            access_level19, explanation_video19 =expl(test_id, 19)

            if correct_answer19 == answer19:
                result = result+1
                color19 = False
            else:
                color19 = True
##########################################

            # redirect to a new URL:
            return render(request, 'egemath/egetestanswer.html', {
            #'test_id': 'test_id',
            'answer1': answer1,
            'correct_answer1' : correct_answer1,
            'color1' : color1,
            'access_level1' : access_level1,
            'explanation_video1' : explanation_video1,

            'answer2' : answer2,
            'correct_answer2' : correct_answer2,
            'color2': color2,
            'access_level2' : access_level2,
            'explanation_video2' : explanation_video2,

            'answer3': answer3,
            'correct_answer3' : correct_answer3,
            'color3': color3,
            'access_level3' : access_level3,
            'explanation_video3' : explanation_video3,

            'answer4': answer4,
            'correct_answer4' : correct_answer4,
            'color4': color4,
            'access_level4' : access_level4,
            'explanation_video4' : explanation_video4,

            'answer5': answer5,
            'correct_answer5' : correct_answer5,
            'color5': color5,
            'access_level5' : access_level5,
            'explanation_video5' : explanation_video5,

            'answer6': answer6,
            'correct_answer6' : correct_answer6,
            'color6': color6,
            'access_level6' : access_level6,
            'explanation_video6' : explanation_video6,

            'answer7': answer7,
            'correct_answer7' : correct_answer7,
            'color7': color7,
            'access_level7' : access_level7,
            'explanation_video7' : explanation_video7,

            'answer8': answer8,
            'correct_answer8' : correct_answer8,
            'color8': color8,
            'access_level8' : access_level8,
            'explanation_video8' : explanation_video8,

            'answer9': answer9,
            'correct_answer9' : correct_answer9,
            'color9': color9,
            'access_level9' : access_level9,
            'explanation_video9' : explanation_video9,

            'answer10': answer10,
            'correct_answer10' : correct_answer10,
            'color10': color10,
            'access_level10' : access_level10,
            'explanation_video10' : explanation_video10,

            'answer11': answer11,
            'correct_answer11' : correct_answer11,
            'color11': color11,
            'access_level11' : access_level11,
            'explanation_video11' : explanation_video11,

            'answer12': answer12,
            'correct_answer12' : correct_answer12,
            'color12': color12,
            'access_level12' : access_level12,
            'explanation_video12' : explanation_video12,

            'answer13': answer13,
            'correct_answer13' : correct_answer13,
            'color13': color13,
            'access_level13' : access_level13,
            'explanation_video13' : explanation_video13,

            'answer14': answer14,
            'correct_answer14' : correct_answer14,
            'color14': color14,
            'access_level14' : access_level14,
            'explanation_video14' : explanation_video14,

            'answer15': answer15,
            'correct_answer15' : correct_answer15,
            'color15': color15,
            'access_level15' : access_level15,
            'explanation_video15' : explanation_video15,

            'answer16': answer16,
            'correct_answer16' : correct_answer16,
            'color16': color16,
            'access_level16' : access_level16,
            'explanation_video16' : explanation_video16,

            'answer17': answer17,
            'correct_answer17' : correct_answer17,
            'color17': color17,
            'access_level17' : access_level17,
            'explanation_video17' : explanation_video17,

            'answer18': answer18,
            'correct_answer18' : correct_answer18,
            'color18': color18,
            'access_level18' : access_level18,
            'explanation_video18' : explanation_video18,

            'answer19': answer19,
            'correct_answer19' : correct_answer19,
            'color19': color19,
            'access_level19' : access_level19,
            'explanation_video19' : explanation_video19,

            'result': result,
            'user_access_level_ege' : user_access_level_ege,
            'test_id': test_id,

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
        question_text_11, question_image_11 = quest(test_id, 11)
        question_text_12, question_image_12 = quest(test_id, 12)

        question_text_13, question_image_13, question_text_1_13, question_text_2_13, question_text_3_13 = quest(test_id, 13)
        answer_text_1_13, answer_text_2_13, answer_text_3_13, answer_text_4_13 = aswertext(test_id, 13)

        question_text_14, question_image_14, question_text_1_14, question_text_2_14, question_text_3_14 = quest(test_id, 14)
        answer_text_1_14, answer_text_2_14, answer_text_3_14, answer_text_4_14 = aswertext(test_id, 14)

        question_text_15, question_image_15, question_text_1_15, question_text_2_15, question_text_3_15 = quest(test_id, 15)
        answer_text_1_15, answer_text_2_15, answer_text_3_15, answer_text_4_15 = aswertext(test_id, 15)

        question_text_16, question_image_16, question_text_1_16, question_text_2_16, question_text_3_16 = quest(test_id, 16)
        answer_text_1_16, answer_text_2_16, answer_text_3_16, answer_text_4_16 = aswertext(test_id, 16)

        question_text_17, question_image_17, question_text_1_17, question_text_2_17, question_text_3_17 = quest(test_id, 17)
        answer_text_1_17, answer_text_2_17, answer_text_3_17, answer_text_4_17 = aswertext(test_id, 17)

        question_text_18, question_image_18, question_text_1_18, question_text_2_18, question_text_3_18 = quest(test_id, 18)
        answer_text_1_18, answer_text_2_18, answer_text_3_18, answer_text_4_18 = aswertext(test_id, 18)

        question_text_19, question_image_19, question_text_1_19, question_text_2_19, question_text_3_19 = quest(test_id, 19)
        answer_text_1_19, answer_text_2_19, answer_text_3_19, answer_text_4_19 = aswertext(test_id, 19)


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

    'question_text_11' : question_text_11,
    'question_image_11': question_image_11,

    'question_text_12' : question_text_12,
    'question_image_12': question_image_12,

    'question_text_13' : question_text_13,
    'question_text_1_13' : question_text_1_13,
    'question_text_2_13' : question_text_2_13,
    'question_text_3_13' : question_text_3_13,
    'question_image_13': question_image_13,
    'answer_text_1_13' : answer_text_1_13,
    'answer_text_2_13' : answer_text_2_13,
    'answer_text_3_13' : answer_text_3_13,
    'answer_text_4_13' : answer_text_4_13,

    'question_text_14' : question_text_14,
    'question_text_1_14' : question_text_1_14,
    'question_text_2_14':question_text_2_14,
    'question_text_3_14':question_text_3_14,
    'question_image_14': question_image_14,
    'answer_text_1_14' : answer_text_1_14,
    'answer_text_2_14' : answer_text_2_14,
    'answer_text_3_14' : answer_text_3_14,
    'answer_text_4_14' : answer_text_4_14,

    'question_text_15' : question_text_15,
    'question_text_1_15' : question_text_1_15,
    'question_text_2_15' : question_text_2_15,
    'question_text_3_15' : question_text_3_15,
    'question_image_15': question_image_15,
    'answer_text_1_15' : answer_text_1_15,
    'answer_text_2_15' : answer_text_2_15,
    'answer_text_3_15' : answer_text_3_15,
    'answer_text_4_15' : answer_text_4_15,

    'question_text_16' : question_text_16,
    'question_text_1_16' : question_text_1_16,
    'question_text_2_16' : question_text_2_16,
    'question_text_3_16' : question_text_3_16,
    'question_image_16': question_image_16,
    'answer_text_1_16' : answer_text_1_16,
    'answer_text_2_16' : answer_text_2_16,
    'answer_text_3_16' : answer_text_3_16,
    'answer_text_4_16' : answer_text_4_16,

    'question_text_17' : question_text_17,
    'question_text_1_17' : question_text_1_17,
    'question_text_2_17' : question_text_2_17,
    'question_text_3_17' : question_text_3_17,
    'question_image_17': question_image_17,
    'answer_text_1_17' : answer_text_1_17,
    'answer_text_2_17' : answer_text_2_17,
    'answer_text_3_17' : answer_text_3_17,
    'answer_text_4_17' : answer_text_4_17,

    'question_text_18' : question_text_18,
    'question_text_1_18' : question_text_1_18,
    'question_text_2_18' : question_text_2_18,
    'question_text_3_18' : question_text_3_18,
    'question_image_18': question_image_18,
    'answer_text_1_18' : answer_text_1_18,
    'answer_text_2_18' : answer_text_2_18,
    'answer_text_3_18' : answer_text_3_18,
    'answer_text_4_18' : answer_text_4_18,

    'question_text_19' : question_text_19,
    'question_text_1_19' : question_text_1_19,
    'question_text_2_19' : question_text_2_19,
    'question_text_3_19' : question_text_3_19,
    'question_image_19': question_image_19,
    'answer_text_1_19' : answer_text_1_19,
    'answer_text_2_19' : answer_text_2_19,
    'answer_text_3_19' : answer_text_3_19,
    'answer_text_4_19' : answer_text_4_19,


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

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
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
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect('signup')

            #password =  form.cleaned_data['password']
            #email =  form.cleaned_data['email']
            #username =  form.cleaned_data['username']

            #if not User.objects.filter(email__contains = email): # пробуем получить уникальную почту на имя пользователя
            #    try:
            #        user = User.objects.create_user(username, email, password)
            #        user.save()
            #        if user is not None:
            #            if user.is_active:
            #                login(request, user)
            #                return redirect('donate')
            #    except  IntegrityError:
            #        return render(request, 'registration/signup.html', {'form': form, 'username_not_uniq': True })
            #else:
            #    return render(request, 'registration/signup.html', {'form': form, 'email_not_uniq': True })
            # redirect to a new URL:
            #return redirect('login')
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

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                username =  form.cleaned_data['username']
                password =  form.cleaned_data['password']
                user = authenticate(username=username, password=password)

                if user is not None:
                    if user.is_active:
                        login(request, user)
                        # Redirect to a success page.
                        return redirect('ege_math')
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




            #messages.success(request, 'New comment added with success!')
            else:
                pass
                #messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect('log')

        #    username =  form.cleaned_data['username']
        #    password =  form.cleaned_data['password']
        #    user = authenticate(username=username, password=password)

        #if user is not None:
        #    if user.is_active:
        #        login(request, user)
        #        # Redirect to a success page.
        #        return redirect('ege_math')
            #else:
                    # Return a 'disabled account' error message
                    #...
                #return render(request, 'registration/login.html', {'form': form, 'password_not_correct': True})
        #else:
                # Return an 'invalid login' error message.
                #...
        #    return render(request, 'registration/login.html', {'form': form, 'password_not_correct': True})
            # redirect to a new URL:
            #return redirect('home_page')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()



    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('ege_math')

def home_page(request):
    return render(request, 'egemath/home.html', {})

def about(request):
            # if this is a POST request we need to process the form data

            if request.method == 'POST':
                # create a form instance and populate it with data from the request:
                form = CustomerApplicationForm(request.POST)

                # check whether it's valid:
                if form.is_valid():
                    # process the data in form.cleaned_data as required
                    # ...

                    сontact_email = form.cleaned_data['сontact_email']
                    сontact_name = form.cleaned_data['сontact_name']
                    email_subscribe = form.cleaned_data['email_subscribe']


                    if сontact_email or contact_phone:
                        #send_mail('application', message, 'admin@testege.com', ['astruslux@gmail.com'])
                        send_mail('Заявка',
                        ' Email: ' + сontact_email + ', '+ ' Имя: '+ сontact_name+','+' Subscribe: ' + str(email_subscribe),
                        'astruslux@gmail.com',
                         ['creativerror@gmail.com'] )


                    # redirect to a new URL:
                    return HttpResponseRedirect('thanks')


            # if a GET (or any other method) we'll create a blank form
            else:
                form = CustomerApplicationForm()

            return render(request, 'egemath/about.html', {'form': form})


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

                contact_phone = form.cleaned_data['сontact_phone']
                сontact_email = form.cleaned_data['сontact_email']
                сontact_name = form.cleaned_data['сontact_name']
                offer_accepted = form.cleaned_data['offer_accepted']
                email_subscribe = form.cleaned_data['email_subscribe']

                if сontact_email or contact_phone:
                    #send_mail('application', message, 'admin@testege.com', ['astruslux@gmail.com'])
                    send_mail('Заявка',
                    'Телефон :  ' + contact_phone +', '+ 'Email: ' + сontact_email + ', '+ 'Имя: '+ сontact_name+','+' Хочу начать заниматься: ' + str(offer_accepted) + ' Subscribe: ' + str(email_subscribe),
                    'astruslux@gmail.com',
                     ['creativerror@gmail.com'] )


                # redirect to a new URL:
                #subject_mail = ''
                return HttpResponseRedirect('thanks')


        # if a GET (or any other method) we'll create a blank form
        else:
            form = CustomerApplicationForm()

        return render(request, 'egemath/repetitor_math.html', {'form': form})


def subscribe(request):
            # if this is a POST request we need to process the form data
            #subject_mail = 'Заявка на подписку'
            if request.method == 'POST':
                # create a form instance and populate it with data from the request:
                form = CustomerApplicationForm(request.POST)
                # check whether it's valid:
                if form.is_valid():
                    # process the data in form.cleaned_data as required
                    # ...

                    сontact_email = form.cleaned_data['сontact_email']
                    сontact_name = form.cleaned_data['сontact_name']
                    email_subscribe = form.cleaned_data['email_subscribe']


                    if сontact_email or contact_phone:
                        #send_mail('application', message, 'admin@testege.com', ['astruslux@gmail.com'])
                        send_mail('Заявка',
                        ' Email: ' + сontact_email + ', '+ ' Имя: '+ сontact_name+','+' Subscribe: ' + str(email_subscribe),
                        'astruslux@gmail.com',
                         ['creativerror@gmail.com'] )


                    # redirect to a new URL:
                    return HttpResponseRedirect('thanks')


            # if a GET (or any other method) we'll create a blank form
            else:
                form = CustomerApplicationForm()

            return render(request, 'egemath/subscribe.html', {'form': form})

def donate(request):
    return render(request, 'egemath/donate.html', {})

def copyright(request):
    return render(request, 'egemath/copyright.html', {})

def todo(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomerApplicationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            сontact_email = form.cleaned_data['сontact_email']
            сontact_name = form.cleaned_data['сontact_name']
            email_subscribe = form.cleaned_data['email_subscribe']


            if сontact_email or contact_phone:
                send_mail('Заявка',
                ' Email: ' + сontact_email + ', '+ ' Имя: '+ сontact_name+','+' Subscribe: ' + str(email_subscribe),
                'astruslux@gmail.com',
                 ['creativerror@gmail.com'] )


            # redirect to a new URL:
            return HttpResponseRedirect('thanks')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomerApplicationForm()

    return render(request, 'egemath/todo.html', {'form': form})

def administrator(request):
    username = str(request.user)
    if request.method == 'POST' and username == 'artem':
        # create a form instance and populate it with data from the request:
        form = AdmistratorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            test_num = form.cleaned_data['test_num']
            task_num = form.cleaned_data['task_num']

            # redirect to a new URL:
            return redirect('ege_test_input', test_num = test_num, task_num = task_num)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AdmistratorForm()
        if username == 'artem':
            return render(request, 'egemath/admistrator.html', {'form': form})
        else:
            return redirect('ege_math')




def ege_test_input(request, test_num, task_num):

    if str(request.user) == 'artem':
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
             #
             instance_data = EgeMathTest.objects.filter(test_num__contains = test_num).filter(task_num__contains = task_num).first()
             if instance_data:
                 form = EgeTestInputForm(request.POST, request.FILES, instance = instance_data)
                 # check whether it's valid:
                 if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                    form.save()
                    return redirect('administrator')
            #else:
                #return redirect('ege_math')
             else:

                 form = EgeTestInputForm(request.POST, request.FILES)
                 if form.is_valid():

                # process the data in form.cleaned_data as required
                # ...
                     form.save()
                     return redirect('administrator')

    # if a GET (or any other method) we'll create a blank form
        else:
            instance_data = EgeMathTest.objects.filter(test_num__contains = test_num).filter(task_num__contains = task_num).first()
            form = EgeTestInputForm(instance = instance_data)
            return render(request, 'egemath/ege_test_input.html', {'form': form, 'test_num' : test_num, 'task_num' : task_num})
    else:
        return redirect('ege_math')


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
