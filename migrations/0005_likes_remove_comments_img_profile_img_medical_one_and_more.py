# Generated by Django 5.0.1 on 2024-03-23 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_blogs_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(verbose_name='like')),
                ('dislike', models.IntegerField(verbose_name='dislike')),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='img',
        ),
        migrations.AddField(
            model_name='profile',
            name='img_medical_one',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='youre picture medical one:'),
        ),
        migrations.AddField(
            model_name='profile',
            name='img_medical_three',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='youre picture medical three:'),
        ),
        migrations.AddField(
            model_name='profile',
            name='img_medical_two',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='youre picture medical two:'),
        ),
    ]
