# Generated by Django 2.2.3 on 2019-07-31 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_allservices_engname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allservices',
            name='engName',
            field=models.CharField(max_length=50),
        ),
    ]