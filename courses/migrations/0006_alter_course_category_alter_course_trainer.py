# Generated by Django 5.1 on 2024-08-30 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_trainer_alter_course_image'),
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='courses.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.trainer'),
        ),
    ]
