# Generated by Django 2.2 on 2020-05-12 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='api_test',
            name='header',
            field=models.TextField(default=' ', verbose_name='请求头'),
        ),
        migrations.AlterField(
            model_name='api_test',
            name='api_test_desc',
            field=models.TextField(blank=True, default=' ', verbose_name='接口描述'),
        ),
        migrations.AlterField(
            model_name='api_test',
            name='api_test_result',
            field=models.TextField(blank=True, default=' ', verbose_name='测试结果'),
        ),
        migrations.AlterField(
            model_name='api_test',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_api_test', to='product.Product', verbose_name='所属项目'),
        ),
    ]