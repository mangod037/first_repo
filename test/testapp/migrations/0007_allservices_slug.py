# Generated by Django 2.2.3 on 2019-07-31 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20190731_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='allservices',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
