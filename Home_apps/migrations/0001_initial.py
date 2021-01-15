# Generated by Django 3.1.5 on 2021-01-13 10:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Story', models.CharField(max_length=500)),
                ('Time_lenght', models.DurationField()),
                ('Makers', models.CharField(max_length=50)),
                ('released_date', models.DateField()),
                ('Languages', models.CharField(max_length=50)),
                ('Poster', models.ImageField(upload_to='movie_poster/')),
            ],
        ),
        migrations.CreateModel(
            name='UserComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Msg', models.CharField(max_length=100)),
                ('Email_id', models.EmailField(max_length=254)),
                ('Date', models.DateTimeField(default=datetime.datetime(2021, 1, 13, 10, 36, 15, 451166))),
                ('Movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home_apps.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File', models.ImageField(upload_to='movie_screenshot/')),
                ('Movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home_apps.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quality_type', models.CharField(max_length=20)),
                ('File', models.CharField(max_length=50)),
                ('Movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home_apps.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home_apps.movie')),
            ],
        ),
    ]
