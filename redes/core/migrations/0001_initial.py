# Generated by Django 2.2 on 2020-01-23 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellido_Paterno', models.CharField(max_length=10)),
                ('apellido_Materno', models.CharField(max_length=10)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
                ('usuario', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
