# Generated by Django 2.2.3 on 2019-07-31 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_auto_20190731_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allservices',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
