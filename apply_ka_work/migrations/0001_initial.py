# Generated by Django 4.2.6 on 2023-11-01 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=80)),
                ('lastname', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('trabaho', models.CharField(max_length=80)),
            ],
        ),
    ]
