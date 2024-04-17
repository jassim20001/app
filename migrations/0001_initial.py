# Generated by Django 5.0.1 on 2024-03-19 13:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('comment', models.CharField(max_length=500, verbose_name='comment')),
                ('img', models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='youre picture')),
            ],
        ),
        migrations.CreateModel(
            name='Comments2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('youremail', models.CharField(max_length=100)),
                ('numberphone', models.IntegerField()),
                ('masseg', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='LOGIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('doctor', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('subtitle', models.CharField(blank=True, max_length=1000, null=True, verbose_name='about you')),
                ('infor', models.TextField(blank=True, max_length=500, null=True, verbose_name='information about you')),
                ('adrees', models.CharField(max_length=50, verbose_name='adress')),
                ('adrees_detail', models.CharField(max_length=80, verbose_name='adrees_detail')),
                ('number_phone', models.IntegerField(blank=True, null=True, verbose_name='number_phone')),
                ('working_hour', models.CharField(max_length=100, verbose_name='working houre')),
                ('working_time', models.CharField(blank=True, max_length=100, null=True, verbose_name='working time')),
                ('doctor_in', models.CharField(blank=True, choices=[('Obesity and endoscopic surgery', 'Obesity and endoscopic surgery'), ('Heart and blood vessels', 'Heart and blood vessels'), ('Blood diseases', 'Blood diseases'), ('Bones', 'Bones'), ('Gynecology and Obstetrics', 'Gynecology and Obstetrics'), ('Newborn babies', 'Newborn babies'), ('teeth', 'teeth'), ('Newborn babies', 'Newborn babies'), ('Nose, Ear and Throat', 'Nose, Ear and Throat'), ('Tumors', 'Tumors')], max_length=50, null=True, verbose_name='doctor_in?')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Detection price:')),
                ('facebook', models.CharField(blank=True, max_length=50, null=True, verbose_name='facebook')),
                ('google', models.CharField(blank=True, max_length=50, null=True, verbose_name='google')),
                ('twitter', models.CharField(blank=True, max_length=50, null=True, verbose_name='twitter')),
                ('img', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='youre picture:')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('tybe', models.CharField(blank=True, choices=[('Male', 'male'), ('Female', 'female')], max_length=50, null=True, verbose_name='tybe:')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profile',
            },
        ),
    ]