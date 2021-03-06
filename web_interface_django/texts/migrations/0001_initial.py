# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-29 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clusters', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag_Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='tags.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plain_text', models.TextField()),
                ('source_url', models.CharField(max_length=512)),
                ('cluster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clusters.Cluster')),
            ],
            options={
                'verbose_name_plural': 'Texts',
                'verbose_name': 'Text',
            },
        ),
        migrations.AddField(
            model_name='tag_text',
            name='text',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='texts.Text'),
        ),
    ]
