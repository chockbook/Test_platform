# Generated by Django 2.2 on 2020-05-23 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0005_auto_20200512_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Web_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_test_name', models.CharField(max_length=64, verbose_name='Web用例名称')),
                ('web_test_desc', models.TextField(default=' ', verbose_name='用例描述')),
                ('web_test_url', models.CharField(max_length=100, verbose_name='页面地址')),
                ('web_test_elem', models.TextField(default=' ', verbose_name='定位语句')),
                ('web_test_method', models.CharField(choices=[('ID', 'ID'), ('classname', 'classname'), ('Xpath', 'xpath'), ('css_seletor', 'css_seletor')], default='ID', max_length=30, verbose_name='定位方式')),
                ('web_test_input', models.CharField(max_length=50, null=True, verbose_name='输入值')),
                ('web_test_plural', models.CharField(choices=[('singular', 'singular'), ('plural', 'plural')], default='singular', max_length=4, verbose_name='单数或复数')),
                ('web_test_result', models.TextField(blank=True, default=' ', verbose_name='预期测试结果')),
                ('web_test_result_finaly', models.TextField(blank=True, default=' ', verbose_name='最终测试结果')),
                ('web_test_bug', models.CharField(choices=[('null', ' '), ('是', '是'), ('否', '否')], default='null', max_length=4, verbose_name='是否有Bug')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_web_test', to='product.Product', verbose_name='所属项目')),
                ('web_test_user', models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='测试人员')),
            ],
            options={
                'verbose_name': 'Web测试',
                'verbose_name_plural': 'Web测试',
            },
        ),
    ]