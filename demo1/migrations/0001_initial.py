# Generated by Django 2.1.7 on 2020-06-20 08:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=16, unique=True, verbose_name='客户端号')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(1)], verbose_name='分数')),
            ],
        ),
        migrations.CreateModel(
            name='Rnk',
            fields=[
                ('c_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='demo1.Score')),
                ('rank', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='名次')),
            ],
        ),
    ]
