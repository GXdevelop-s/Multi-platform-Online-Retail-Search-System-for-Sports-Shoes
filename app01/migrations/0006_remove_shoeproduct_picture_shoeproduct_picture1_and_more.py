# Generated by Django 4.2.1 on 2023-05-12 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_alter_recomkey_key1_alter_recomkey_key2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoeproduct',
            name='picture',
        ),
        migrations.AddField(
            model_name='shoeproduct',
            name='picture1',
            field=models.CharField(default='待修改', max_length=300, verbose_name='图片1'),
        ),
        migrations.AddField(
            model_name='shoeproduct',
            name='picture2',
            field=models.CharField(default='待修改', max_length=300, verbose_name='图片2'),
        ),
        migrations.AddField(
            model_name='shoeproduct',
            name='picture3',
            field=models.CharField(default='待修改', max_length=300, verbose_name='图片3'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_choice',
            field=models.SmallIntegerField(choices=[(1035, '跑鞋'), (9914, '徒步鞋'), (1034, '足球鞋'), (1032, '篮球鞋'), (5853, '羽毛球鞋'), (10106, '轮滑鞋'), (10304, '综合训练鞋'), (1033, '舞蹈鞋'), (7429, '高尔夫球鞋'), (9906, '运动凉鞋')], null=True, verbose_name='上一次的选择'),
        ),
        migrations.AlterField(
            model_name='recomkey',
            name='key2',
            field=models.SmallIntegerField(choices=[(3, '复古'), (4, '简约'), (2, '经典'), (1, '时尚')], verbose_name='关键字2'),
        ),
    ]
