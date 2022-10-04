from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'pages-login.html')


def home(request):
    if not request.user.is_active:
        return redirect('index')
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Tài khoản hoặc mật khẩu sai')
            return redirect('index')
    else:
        return render(request, 'pages-login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def user_profile(request):
    if not request.user.is_active:
        return redirect('index')
    return render(request, 'users-profile.html')


def overview(request):
    users = {
        'user': request.user
    }
    return render(request, 'users-profile.html', users)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2 and password1 != '':
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Tên đăng nhập đã sử dụng')
                return redirect('user_profile')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email đã sử dụng')
                return redirect('user_profile')

            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'Đăng ký thành công')
                return redirect('user_profile')
        else:
            messages.info(
                request, 'Mật khẩu trống hoặc mật khẩu chưa trùng khớp khớp với nhau')
            return redirect('user_profile')
    else:
        return render(request, 'users-profile.html')


def change_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        new_password = request.POST['new_password']

        user = User.objects.get(username__exact=username)
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Đổi mật khẩu thành công')
        return redirect('index')
    else:
        return render(request, 'users-profile.html')
