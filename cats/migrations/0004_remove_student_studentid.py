# Generated by Django 2.2 on 2024-03-20 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_student_studentid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='studentID',
        ),
    ]