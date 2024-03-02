# Generated by Django 4.2.1 on 2023-05-16 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_rename_admin_id_advertisement_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.admin', verbose_name='管理员id'),
        ),
        migrations.AlterField(
            model_name='recomkey',
            name='key2',
            field=models.SmallIntegerField(choices=[(2, '经典'), (3, '复古'), (4, '简约'), (1, '时尚'), (5, '奇异')], null=True, verbose_name='风格'),
        ),
        migrations.AlterField(
            model_name='recomkey',
            name='key3',
            field=models.SmallIntegerField(choices=[(3, '低价'), (1, '高级'), (2, '平价')], null=True, verbose_name='价位'),
        ),
    ]
