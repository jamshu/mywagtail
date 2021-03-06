# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-14 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170414_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientHomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.Client')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='testimonial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.Client'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='testimonial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.Client'),
        ),
        migrations.AddField(
            model_name='clienthomepage',
            name='homepage',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='home.HomePage'),
        ),
        migrations.AddField(
            model_name='clientaboutpage',
            name='aboutpage',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='home.AboutPage'),
        ),
        migrations.AddField(
            model_name='clientaboutpage',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.Client'),
        ),
    ]
