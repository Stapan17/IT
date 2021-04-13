from django.shortcuts import render, redirect
from .forms import userForm, userInfoForm, userInfoUpdateForm, jobPostForm
from .models import userInfo, User, jobPost, contactUS
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import smtplib


def base(request):
    return render(request, 'base.html')


def home(request):

    objects = jobPost.objects.all().order_by('-id')
    context = {}

    if request.user.is_authenticated:
        current_user = request.user
        current_user_info = userInfo.objects.get(member_id=current_user.id)
        context = {'current_user': current_user,
                   'current_user_info': current_user_info, 'objects': objects}

    else:
        context = {'objects': objects}

    return render(request, 'home.html', context)


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


def profile(request, pk):
    current_user = User.objects.get(id=pk)
    current_user_info = userInfo.objects.get(member_id=pk)

    context = {'current_user': current_user,
               'current_user_info': current_user_info}
    return render(request, 'user/profile.html', context)


def update(request, pk):
    current_user = User.objects.get(id=pk)
    form = userForm(instance=current_user)

    current_user_info = userInfo.objects.get(member_id=pk)
    Object = current_user_info
    info_form = userInfoForm(instance=current_user_info)

    if request.POST:

        formUpdate = userInfoUpdateForm(
            request.POST, request.FILES, instance=current_user_info)
        username = request.POST.get('username')
        email = request.POST.get('email')

        flag = True

        if User.objects.filter(username=username).exists():
            if User.objects.get(username=username).id == pk:
                flag = False

        if formUpdate.is_valid() and flag:
            current_user.username = username
            current_user.email = email
            current_user.save()

            obj = formUpdate.save(commit=False)
            obj.save()

            info_form = obj
            return redirect('home')

        else:
            error = "Username already Exists, try something else"

            context = {'form': form, 'info_form': info_form,
                       'error': error, 'Object': Object, 'current_user': current_user}
            return render(request, 'user/update.html', context)

    info_form = userInfoUpdateForm(instance=current_user_info)

    context = {'form': form, 'info_form': info_form,
               'Object': Object, 'current_user': current_user}
    return render(request, 'user/update.html', context)


def job_post(request):

    curr_user = request.user
    pk = curr_user.id
    current_user = User.objects.get(id=pk)
    current_user_info = userInfo.objects.get(member_id=pk)
    context = {'form': jobPostForm, 'current_user': current_user,
               'current_user_info': current_user_info}
    if request.method == "POST":
        form = jobPostForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')

        else:
            print("ERROR")
            print(form.errors)
            context = {'form': jobPostForm, 'current_user': current_user,
                       'current_user_info': current_user_info, 'form.errors': form.errors}

    return render(request, 'job/postForm.html', context)


def manage_post(request, pk):
    curr_user = request.user
    current_user = User.objects.get(id=pk)
    current_user_info = userInfo.objects.get(member_id=pk)
    curr_user_post = jobPost.objects.filter(person_id=pk)

    context = {'curr_user_post': curr_user_post,
               'current_user': current_user, 'current_user_info': current_user_info}
    return render(request, 'job/managePost.html', context)


def error(request):
    return render(request, 'error.html')


def update_post(request, pk):
    Object = jobPost.objects.get(id=pk)
    form = jobPostForm(instance=Object)

    if request.method == 'POST':
        form_data = jobPostForm(request.POST, instance=Object)

        if form_data.is_valid():
            form_data.save()
            return redirect('home')

        else:
            print(form_data.errors)

    context = {'form': form}
    return render(request, 'job/updatePost.html', context)


def delete_post(request, pk):
    Object = jobPost.objects.get(id=pk)

    if request.method == 'POST':
        Object.delete()
        return redirect('home')

    context = {'Object': Object}
    return render(request, 'job/deletePost.html', context)


def detail_post(request, pk):

    post = jobPost.objects.get(id=pk)
    current_user = request.user
    current_user_info = userInfo.objects.get(member_id=current_user.id)
    context = {'post': post, 'current_user': current_user,
               'current_user_info': current_user_info}
    return render(request, 'job/detailPost.html', context)


def contact(request):
    if request.method == 'POST':
        form = contactUS()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        form.name = name
        form.mail = email
        form.message = message
        form.save()
        return redirect('home')
    return render(request, 'contact.html')


def admin(request):
    return render(request, 'admin.html')
