# Generated by Django 2.2 on 2024-03-20 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('numCats', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.Student')),
            ],
        ),
    ]
