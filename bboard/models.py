from django.db import models
from django.utils.text import slugify
from django.core import validators


# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    slug = models.SlugField(blank=True, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Bb, self).save()

    class CITIES(models.TextChoices):
        KYIV = 'kyi', 'Киев'
        ODESSA = 'ode', 'Одесса'
        DNIPRO = 'dni', 'Днепр'
        __empty__ = '---------'

    city = models.CharField(max_length=3, choices=CITIES.choices)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-date']
        unique_together = (('title', 'date'),
                           ('title', 'rubric', 'date'))


class Rubric(models.Model):
    name = models.CharField(max_length=40, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']

