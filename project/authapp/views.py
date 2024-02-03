from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')
        if get_password != get_confirm_password:
            messages.info(request, 'Password is not matching')
            return redirect('/auth/signup')

        try:
            if User.objects.get(username=get_email):
                messages.warning(request, "Email is not taken")
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass

        my_user=User.objects.create_user(get_email,get_email,get_password)
        my_user.save()
        messages.success(request, "User is created please login")
        return redirect('/auth/login')

    return render(request, 'signup.html')

def handleLogin(request):
    return render(request, 'login.html')

def handleLogout(request):
    return render(request, 'login.html')