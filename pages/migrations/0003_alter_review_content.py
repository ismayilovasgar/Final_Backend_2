# Generated by Django 5.1 on 2024-08-31 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_review_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(default="The greatest fitness app. It's clear the makers behind this thing use it every week, because it is so perfect.", max_length=250),
        ),
    ]
