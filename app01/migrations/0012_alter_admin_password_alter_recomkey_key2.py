# Generated by Django 4.2.1 on 2023-05-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_alter_recomkey_key2_alter_user_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=100, verbose_name='管理员密码'),
        ),
        migrations.AlterField(
            model_name='recomkey',
            name='key2',
            field=models.SmallIntegerField(choices=[(3, '复古'), (1, '时尚'), (4, '简约'), (2, '经典')], verbose_name='关键字2'),
        ),
    ]
