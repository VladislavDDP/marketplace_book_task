from django.contrib.postgres.operations import BtreeGistExtension, CITextExtension
from django.db import models, migrations
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Machine(models.Model):
    name = models.CharField(max_length=30, verbose_name='Машина')
    spare = models.ManyToManyField('Spare', through='Kit',
                                   through_fields=('machine', 'spare'),
                                   verbose_name='Деталь')


class Spare(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название детали')


class Kit(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество деталей')


class Note(models.Model):
    content = models.TextField(verbose_name='Содержание')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField(verbose_name='Id')
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')
