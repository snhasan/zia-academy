# Generated by Django 2.0.7 on 2020-05-03 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogs', '0003_auto_20200502_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='myBlog_comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.IntegerField(max_length=11)),
                ('comentor_name', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='myblog',
            name='comentor_name',
        ),
        migrations.RemoveField(
            model_name='myblog',
            name='email',
        ),
        migrations.RemoveField(
            model_name='myblog',
            name='message',
        ),
    ]
