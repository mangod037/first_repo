# Generated by Django 2.2.1 on 2019-05-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=30),
        ),
    ]
