from .models import News_film
from django.forms import ModelForm, TextInput

class News_filmForm(ModelForm):
	class Meta:
		model = News_film
		fields = ['title', 'director', 'short_description', 'comment']

widgets = {
        'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
        'director': TextInput(attrs={'class': 'form-control', 'placeholder': 'Режисер'}),
        'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
        'comment': TextInput(attrs={'class': 'form-control', 'placeholder': 'Коментарий к фильму'})
}