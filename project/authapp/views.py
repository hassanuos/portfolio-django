from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == 'POST':
        get_email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')
        if get_password != get_confirm_password:
            messages.info(request, 'Password is not matching')
            return redirect('/auth/signup')

        try:
            if User.objects.get(username=get_email):
                messages.warning(request, "Email already taken")
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass

        new_user = User.objects.create_user(get_email, get_email, get_password)
        new_user.is_active = True
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()

        my_user = authenticate(username=get_email, password=get_password)
        if my_user is not None:
            login(request, my_user)
            messages.success(request, "User created & Login successful!!!")
            return redirect('/')
        # messages.success(request, "User is created please login")
        # return redirect('/auth/login')

    return render(request, 'signup.html')


def handleLogin(request):
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')

        my_user = authenticate(username=get_email, password=get_password)
        if my_user is not None:
            login(request, my_user)
            messages.success(request, "Login success")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials!!!")
    return render(request, 'login.html')


def handleLogout(request):
    logout(request)
    messages.success(request, "logout successfully")
    return render(request, 'login.html')
