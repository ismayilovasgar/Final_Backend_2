# Generated by Django 5.1 on 2024-08-24 20:46

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_profession_category_remove_trainer_profession_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='category',
            field=models.CharField(choices=[('Yoga', 'Yoga'), ('Fitness', 'Fitness & Gym'), ('Gymnastics', 'Gymnastics'), ('Running', 'Running')], default='Yoga', help_text='Select the category of the product.', max_length=25),
        ),
        migrations.AddField(
            model_name='trainer',
            name='difficulty_level',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='Intermediate', help_text='Select the difficulty level of the task.', max_length=25),
        ),
        migrations.AddField(
            model_name='trainer',
            name='intensity_level',
            field=models.CharField(choices=[('level_1', 'Level 1'), ('level_2', 'Level 2'), ('level_3', 'Level 3')], default='level_2', help_text='Select the intensity level of the exercise.', max_length=25),
        ),
        migrations.AddField(
            model_name='trainer',
            name='move_image',
            field=models.ImageField(default='move_avatar.jpg', upload_to=home.models.get_image_upload_path),
        ),
        migrations.AddField(
            model_name='trainer',
            name='move_title',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='time_of_day',
            field=models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], default='morning', help_text='Select the time of day for this schedule.', max_length=25),
        ),
        migrations.AddField(
            model_name='trainer',
            name='yoga_style',
            field=models.CharField(choices=[('morning', 'Morning Yoga'), ('vinyasa', 'Vinyasa Yoga'), ('acro', 'Acro Yoga')], default='morning', help_text='Select the style of yoga for this session.', max_length=25),
        ),
    ]
