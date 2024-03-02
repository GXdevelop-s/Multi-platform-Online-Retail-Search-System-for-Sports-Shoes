# Generated by Django 4.2.1 on 2023-05-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_alter_recomkey_key2_alter_shoeproduct_picture1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomkey',
            name='key2',
            field=models.SmallIntegerField(choices=[(1, '时尚'), (2, '经典'), (3, '复古'), (4, '简约')], verbose_name='关键字2'),
        ),
        migrations.AlterField(
            model_name='shoeproduct',
            name='picture2',
            field=models.ImageField(upload_to='images/', verbose_name='图片2'),
        ),
        migrations.AlterField(
            model_name='shoeproduct',
            name='picture3',
            field=models.ImageField(upload_to='images/', verbose_name='图片3'),
        ),
    ]
