# Generated by Django 5.1 on 2024-08-28 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_trainer_main_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainer',
            options={'ordering': ['created_date']},
        ),
        migrations.RenameField(
            model_name='trainer',
            old_name='started_date',
            new_name='created_date',
        ),
    ]
