# Generated by Django 3.0.8 on 2020-07-19 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tc_manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcase',
            old_name='project_id',
            new_name='project',
        ),
    ]
