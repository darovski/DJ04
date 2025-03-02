from django.shortcuts import render, redirect
from .models import News_film
from .forms import News_filmForm

def index(request):
    news = News_film.objects.all()
    return render(request, 'films/index.html', {'news': news})

def film(request):
    news = News_film.objects.all()
    return render(request, 'films/film.html', {'news': news})

def create_comment_films(request):
    error = ''
    if request.method == 'POST':
        form = News_filmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films')
        else:
            error = "Данные были заполнены некорректно"
    form = News_filmForm()
    return render(request, 'films/comment.html', {'form': form,'error': error})