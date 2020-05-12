# Generated by Django 2.2 on 2020-05-12 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0002_auto_20200512_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_test',
            name='api_test_user',
            field=models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='测试人员'),
        ),
    ]