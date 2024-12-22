from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserReg


# Create your views here.

def sign_up_by_html(request):
    users = ['Tim', 'Tom']
    info = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if (username not in users) and (repeat_password in password) and int(age)>18:
            users.append(username)
            info['OK'] = f'Приветствуем, {username}!'

        else:
            if username in users:
                info['error'] = 'Пользователь уже существует'
            if repeat_password not in password:
                info ['error'] = 'Пароли не совпадают'
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

    return render(request,'registration_page.html', context=info)





def sign_up_by_django(request):
    users = ['Tim', 'Tom']
    info = {}

    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']


            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif repeat_password != password:
                    info['error'] = 'Пароли не совпадают'
            elif age < 18:
                    info['error'] = 'Вы должны быть старше 18'
            else:
                info['OK'] = f'Приветствуем, {username}!'
                users.append(username)
            return render(request, 'registration_page.html', context=info)
    else:
        form = UserReg()
        info['form'] = form

    return render(request, 'registration_page.html', context=info)

