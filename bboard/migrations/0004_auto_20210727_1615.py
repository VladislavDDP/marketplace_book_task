# Generated by Django 3.2.5 on 2021-07-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_bb_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='city',
            field=models.CharField(choices=[(None, '---------'), ('kyi', 'Киев'), ('ode', 'Одесса'), ('dni', 'Днепр')], max_length=3),
        ),
        migrations.AlterUniqueTogether(
            name='bb',
            unique_together={('title', 'date'), ('title', 'rubric', 'date')},
        ),
    ]
