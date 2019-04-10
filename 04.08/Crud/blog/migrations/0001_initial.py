# Generated by Django 2.2 on 2019-04-09 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('review', models.TextField()),
                ('price', models.FloatField()),
                ('score', models.CharField(max_length=10)),
            ],
        ),
    ]
