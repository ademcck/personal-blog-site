from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from post.models import Post
from .forms import LoginForm,  RegisterForm, UserForm, ProfileForm , Privacy, PrivacyForm
from .models import Profile
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import os
# Create your views here.

def myposts(request):
    user = User.objects.get(username = request.user.username) 
    posts = user.posts.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'accounts/myposts.html',{'posts':page_obj})

def accontdelete(request):
    if not request.user.is_authenticated:
        Http404()
    if User.objects.get(username = request.user.username):
        User.objects.get(username = request.user.username).delete()
        return HttpResponseRedirect('/')

def my_account(request):
    
    user_data = {
        'username': request.user.username,
        'email' : request.user.email,
        'fullName': request.user.get_full_name,
    }
    return render(request, 'accounts/myaccount.html', user_data)

def update_profile(request):
    if request.method == 'POST':
        if request.FILES:
            try:
                os.remove(request.user.profile.avatar.path)
            except FileExistsError:
                print("resim bulunamadı")        
            except PermissionError:
                print("permissionError")
            except ValueError:
                print("valueError")
            except:
                pass

        user_form = UserForm(request.POST, instance=request.user)
        privacy_form = PrivacyForm(request.POST or None, instance=request.user.privacy)
        try:
            profile_form = ProfileForm( request.POST,
                                        request.FILES, 
                                        instance=request.user.profile)
        except:
            profile_form = ProfileForm( request.POST,
                                        request.FILES, 
                                        instance=Profile(user=request.user))

        if user_form.is_valid() and profile_form.is_valid():
            
            user_form.save()
            profile_form.save()
            privacy_form.save()
            print('burada')
            return redirect('accounts:profile')
        else:
            pass
    else:
        user_form = UserForm(instance=request.user)
        privacy_form = PrivacyForm(instance = request.user.privacy)
        try:
            profile_form = ProfileForm(instance=request.user.profile)
        except:

            profile_form = ProfileForm(instance=Profile(user=request.user))
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'privacy_form': privacy_form
    }
    return render(request, 'accounts/profile.html', context)



def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request, user) 
        return redirect('post:index')
    return render(request, 'accounts/form.html', {'form': form, 'title': 'Giriş Yap'})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.is_staff =  True
        user.save()
        new_user = authenticate(username = user.username, password=password)
        login(request,new_user)
        return redirect('post:index')
    return render(request, 'accounts/form.html', {'form': form, 'title': 'Üye Ol'})

def get_user_profile(request,username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'accounts/profile_detail.html', context)


def logout_view(request):
    logout(request)
    return redirect('post:index')
