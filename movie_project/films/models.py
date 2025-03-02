from django.db import models

class News_film(models.Model):
	title = models.CharField('Название фильма', max_length=50)
	director = models.CharField('Режисер', max_length=50, default='NoName')
	short_description = models.CharField('Описание фильма', max_length=200)
	comment = models.TextField('Отзыв')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Фильм'
		verbose_name_plural = 'Фильмы'