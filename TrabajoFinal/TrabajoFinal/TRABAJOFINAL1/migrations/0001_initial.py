# Generated by Django 4.1.6 on 2023-02-23 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='iniciarsesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellidos', models.CharField(max_length=30)),
                ('Mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='registracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellidos', models.CharField(max_length=30)),
                ('Mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
