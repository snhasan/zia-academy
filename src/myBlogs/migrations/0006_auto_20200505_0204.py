# Generated by Django 2.0.7 on 2020-05-04 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogs', '0005_delete_myblog_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='myblog',
            name='comentor_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='myblog',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='myblog',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
