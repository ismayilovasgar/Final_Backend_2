# Generated by Django 5.1 on 2024-08-31 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_intensity_level_style_timeofday_course_intensity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='style',
            old_name='NameError',
            new_name='name',
        ),
    ]
