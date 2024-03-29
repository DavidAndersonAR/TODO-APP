# Generated by Django 5.0 on 2023-12-28 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2023-12-28')),
                ('due_date', models.DateField(default='2023-12-28')),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todolist.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
