# Generated by Django 4.2.1 on 2023-05-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_shoeproduct_details_alter_recomkey_key2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomkey',
            name='key2',
            field=models.SmallIntegerField(choices=[(4, '简约'), (1, '时尚'), (2, '经典'), (3, '复古')], verbose_name='关键字2'),
        ),
        migrations.AlterField(
            model_name='shoeproduct',
            name='picture1',
            field=models.ImageField(upload_to='images/', verbose_name='图片1'),
        ),
        migrations.AlterField(
            model_name='shoeproduct',
            name='picture2',
            field=models.ImageField(upload_to='images/', verbose_name='图片1'),
        ),
        migrations.AlterField(
            model_name='shoeproduct',
            name='picture3',
            field=models.ImageField(upload_to='images/', verbose_name='图片1'),
        ),
    ]