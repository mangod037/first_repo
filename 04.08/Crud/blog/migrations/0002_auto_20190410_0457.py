# Generated by Django 2.2 on 2019-04-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='score',
        ),
        migrations.AddField(
            model_name='post',
            name='starScore',
            field=models.CharField(choices=[('1', '★'), ('2', '★★'), ('3', '★★★'), ('4', '★★★★'), ('5', '★★★★★')], default='1', max_length=2),
        ),
    ]
