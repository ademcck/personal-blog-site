from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import widgets
from django.forms.widgets import EmailInput
from accounts.models import Profile , Privacy
from captcha.fields import ReCaptchaField


class UserForm(forms.ModelForm):
    #captcha = ReCaptchaField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name', 
            'email',
        ]
class ProfileForm(forms.ModelForm):
    #captcha = ReCaptchaField()
    
    class Meta:
        model = Profile
        fields = [
            'personel_site',
            'linkedin',
            'facebook',
            'instagram',
            'location',
            'phone',
            'bio',
            'avatar',
        ]
    
class PrivacyForm(forms.ModelForm):
    class Meta:
        model = Privacy
        fields = ['choices_data']

        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,label='Kullanıcı Adı')
    password = forms.CharField(max_length=100,label='Parola', widget=forms.PasswordInput)
    #captcha = ReCaptchaField()

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError("Hatalı Kullanıcı Adı Veya Parola!",code="invalid")
        return super(LoginForm, self).clean()



class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100,label='Kullanıcı Adı')
    password = forms.CharField(max_length=100,label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100,label='Parola Tekrar', widget=forms.PasswordInput)
    email = forms.CharField(widget=EmailInput)
    #captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
            'email',
            
        ]
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Parolalar Eşleşmemektedir")
        return password2



