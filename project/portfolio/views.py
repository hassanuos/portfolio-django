from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('num')
        message = request.POST.get('message')

        query=Contact(name=name,email=email,phonenumber=phone,description=message)
        query.save()
        # print(name, email, phone, message)
        messages.info(request, "Thanks for contacting. We will get back to you soon.")
        return redirect('/contact')

    return render(request, 'contact.html')

def blog(request):
    posts=Blogs.objects.all()
    context={"posts": posts}
    return render(request, 'handleblog.html', context)