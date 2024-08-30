# Generated by Django 5.1 on 2024-08-30 18:11

import trainers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40)),
                ('profession', models.CharField(max_length=40)),
                ('image', models.ImageField(default='profile.jpg', upload_to=trainers.models.get_image_upload_path)),
                ('facebook', models.URLField(blank=True, default='https://www.facebook.com/', max_length=100, null=True)),
                ('twitter', models.URLField(blank=True, default='https://twitter.com/', max_length=100, null=True)),
                ('instagram', models.URLField(blank=True, default='https://www.instagram.com/', max_length=100, null=True)),
                ('linkedin', models.URLField(blank=True, default='https://www.linkedin.com', max_length=100, null=True)),
            ],
        ),
    ]
