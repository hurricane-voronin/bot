# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.TextField()),
                ('response', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeleUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField()),
                ('username', models.CharField(max_length=255)),
                ('uni_api_key', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='chatlog',
            name='telegram_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TeleUser'),
        ),
    ]
