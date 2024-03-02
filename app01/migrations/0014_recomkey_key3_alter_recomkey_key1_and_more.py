# Generated by Django 4.2.1 on 2023-05-14 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_alter_recomkey_key2_alter_user_last_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomkey',
            name='key3',
            field=models.SmallIntegerField(choices=[(2, '平价'), (3, '低价'), (1, '高级')], null=True, verbose_name='关键字2'),
        ),
        migrations.AlterField(
            model_name='recomkey',
            name='key1',
            field=models.SmallIntegerField(choices=[(1035, '跑鞋'), (9914, '徒步鞋'), (1032, '篮球鞋'), (1034, '足球鞋'), (5853, '羽毛球鞋'), (10106, '轮滑鞋'), (10304, '综合训练鞋'), (1033, '舞蹈鞋'), (7429, '高尔夫球鞋'), (9906, '运动凉鞋')], null=True, verbose_name='关键字1'),
        ),
        migrations.AlterField(
            model_name='recomkey',
            name='key2',
            field=models.SmallIntegerField(choices=[(1, '时尚'), (4, '简约'), (2, '经典'), (5, '奇异'), (3, '复古')], null=True, verbose_name='关键字2'),
        ),
    ]
