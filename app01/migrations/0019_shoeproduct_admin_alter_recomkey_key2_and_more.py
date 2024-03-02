# Generated by Django 4.2.1 on 2023-05-19 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0018_alter_recomkey_key2_alter_recomkey_key3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoeproduct',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app01.admin', verbose_name='管理员id'),
        ),
        migrations.AlterField(
            model_name='recomkey',
            name='key2',
            field=models.SmallIntegerField(choices=[(4, '简约'), (2, '经典'), (5, '奇异'), (3, '复古'), (1, '时尚')], null=True, verbose_name='风格'),
        ),
        migrations.AlterField(
            model_name='recomkey',
            name='key3',
            field=models.SmallIntegerField(choices=[(1, '高级'), (2, '平价'), (3, '低价')], null=True, verbose_name='价位'),
        ),
    ]
