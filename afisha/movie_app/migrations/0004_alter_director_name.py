# Generated by Django 4.0.6 on 2022-08-03 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
