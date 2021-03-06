# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=50)),
                ('academician_name', models.CharField(max_length=50)),
                ('faculty', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Department'),
        ),
    ]
