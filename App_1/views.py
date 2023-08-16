from django.shortcuts import render, redirect
from .models import Publications, Forum_Publications
from .forms import forum_publications_form, RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, 'App_1/home_page.html')

def forum_page(request):
    entry = Forum_Publications.objects.order_by('-date')
    return render(request, 'App_1/forum_page.html', {'entry': entry})

@login_required
def site_news(request):
    news = Publications.objects.order_by('-date')
    return render(request, 'App_1/site_news.html', {'news': news})

@login_required
def creating_record_views(request):
    error = ''
    if request.method == 'POST':
        form = forum_publications_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_page')
        else:
            error = 'Форма була неправильно заповнена'
    else:
        form = forum_publications_form()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'App_1/create_record_html.html', data)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home_page')
    else:
        form = RegistrationForm()
    return render(request, 'App_1/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})
