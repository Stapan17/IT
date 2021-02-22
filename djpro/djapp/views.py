from django.shortcuts import render, redirect
from .forms import userForm, userInfoForm
from .models import userInfo, User
from django.contrib.auth import authenticate, login, logout


def home(request):

    return render(request, 'home.html')


def signup(request):

    if request.method == 'POST':
        user_form = userForm(request.POST)
        user_info_form = userInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.member = user
            user_info.save()

            login(request, user)

            return redirect('home')

        else:
            context = {
                'user_form.errors': user_form.errors, 'user_info_form.errors': user_info_form.errors,
                'user_form': user_form, 'user_info_form': user_info_form
            }
            return render(request, 'user/signup.html', context)

    else:
        user_form = userForm()
        user_info_form = userInfoForm()

        context = {'user_form': user_form, 'user_info_form': user_info_form}
        return render(request, 'user/signup.html', context)


def signin(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

        else:
            return redirect('signin')

    else:
        return render(request, 'user/signin.html')


def signout(request):
    logout(request)
    return redirect('home')
