from django import forms

class UserReg(forms.Form):

    username = forms.CharField(max_length=30, label="Введите логин", required=True)
    password = forms.CharField(min_length=8, label="Введите пароль")
    repeat_password = forms.CharField(min_length=8, label="Повторите пароль")
    age = forms.IntegerField(max_value=3,label="Введите свой возраст")

