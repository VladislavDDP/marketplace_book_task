# Generated by Django 3.2.5 on 2021-07-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20210712_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='city',
            field=models.CharField(choices=[('k', 'kiev'), ('od', 'odessa'), ('lv', 'lvov')], default='k', max_length=2),
        ),
    ]
