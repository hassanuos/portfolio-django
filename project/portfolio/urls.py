from django.urls import path
from portfolio import views
urlpatterns = [
    path('', views.home, name='home.html'),
    path('about', views.about, name='about.html'),
    path('contact', views.contact, name='contact.html'),
    path('blog', views.blog, name='handleblog.html'),
]