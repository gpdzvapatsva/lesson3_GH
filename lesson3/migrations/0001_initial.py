# Generated by Django 5.1 on 2024-10-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('student_id', models.IntegerField()),
                ('course', models.CharField(max_length=30)),
            ],
        ),
    ]
