# Generated by Django 2.2.3 on 2019-07-31 01:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20190731_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedservice',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
