# Generated by Django 4.0.1 on 2022-07-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JKNGO', '0004_person_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=500)),
                ('plant_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='rupees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('cardno', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('rupee', models.IntegerField()),
            ],
        ),
    ]
