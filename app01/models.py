from django.db import models


# Create your models here.
class Admin(models.Model):
    '''管理员表'''
    admin_name = models.CharField(verbose_name='管理员名称', max_length=10, null=False)
    password = models.CharField(verbose_name='管理员密码', max_length=100, null=False)


class User(models.Model):
    '''用户表'''
    name = models.CharField(verbose_name='名字', max_length=32, null=False)
    password = models.CharField(verbose_name='密码', max_length=100, null=False)
    age = models.IntegerField(verbose_name='年龄', null=True)
    occupation = models.CharField(verbose_name='职业', max_length=10, null=True)
    gender_choice = (
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choice, null=False)
    admin = models.ForeignKey(verbose_name='管理员编号', to=Admin, to_field='id', on_delete=models.SET_NULL, null=True,
                              default=1)
    type_choice = (
        (1035, '跑鞋'),
        (9914, '徒步鞋'),
        (1034, '足球鞋'),
        (1032, '篮球鞋'),
        (5853, '羽毛球鞋'),
        (10106, '轮滑鞋'),
        (10304, '综合训练鞋'),
        (1033, '舞蹈鞋'),
        (7429, '高尔夫球鞋'),
        (9906, '运动凉鞋')
    )
    last_choice = models.SmallIntegerField(verbose_name='上一次的选择', choices=type_choice, null=True, default=1035)


class ShoeProduct(models.Model):
    '''鞋类产品表'''
    type_choice = (
        (1035, '跑鞋'),
        (9914, '徒步鞋'),
        (1034, '足球鞋'),
        (1032, '篮球鞋'),
        (5853, '羽毛球鞋'),
        (10106, '轮滑鞋'),
        (10304, '综合训练鞋'),
        (1033, '舞蹈鞋'),
        (7429, '高尔夫球鞋'),
        (9906, '运动凉鞋')
    )
    type = models.SmallIntegerField(verbose_name='鞋产品种类', choices=type_choice)
    picture1 = models.ImageField(verbose_name='图片1', upload_to='images/')
    details1 = models.TextField(verbose_name='产品类型描述1', null=False, default='暂无')
    picture2 = models.ImageField(verbose_name='图片2', upload_to='images/')
    details2 = models.TextField(verbose_name='产品类型描述2', null=False, default='暂无')
    picture3 = models.ImageField(verbose_name='图片3', upload_to='images/')
    details3 = models.TextField(verbose_name='产品类型描述3', null=False, default='暂无')
    rank_link = models.CharField(verbose_name='榜单链接', max_length=64)
    admin = models.ForeignKey(verbose_name='管理员id', to=Admin, to_field='id', null=True, on_delete=models.DO_NOTHING)


class RecomKey(models.Model):
    '''推荐关键字表'''
    # 推荐关键字应给定关键字，不能随意设置
    key1_choice = (
        # 该关键字聚焦于种类
        (1035, '跑鞋'),
        (9914, '徒步鞋'),
        (1032, '篮球鞋'),
        (1034, '足球鞋'),
        (5853, '羽毛球鞋'),
        (10106, '轮滑鞋'),
        (10304, '综合训练鞋'),
        (1033, '舞蹈鞋'),
        (7429, '高尔夫球鞋'),
        (9906, '运动凉鞋')
    )
    key2_choice = {
        # 该关键字聚焦风格
        (1, '时尚'),
        (2, '经典'),
        (3, '复古'),
        (4, '简约'),
        (5, '奇异')
    }
    key3_choice = {
        (1, '高级'),
        (2, '平价'),
        (3, '低价')
    }
    key1 = models.SmallIntegerField(verbose_name='类型', choices=key1_choice, null=True)
    key2 = models.SmallIntegerField(verbose_name='风格', choices=key2_choice, null=True)
    key3 = models.SmallIntegerField(verbose_name='价位', choices=key3_choice, null=True)
    band = models.CharField(verbose_name='品牌', max_length=10, null=True)
    # 用户用关键字进行搜索，所以是用户自己的关键字
    user = models.ForeignKey(verbose_name='用户编号', to=User, to_field='id', on_delete=models.CASCADE, unique=True)
    # 鞋类的种类和key1对应
    shoe_product = models.ForeignKey(verbose_name='鞋类产品id', to=ShoeProduct, to_field='id',
                                     on_delete=models.SET_NULL, null=True)


class Advertisement(models.Model):
    owner = models.CharField(verbose_name='广告商', max_length=30)
    ad_picture = models.ImageField(verbose_name='广告图片', upload_to='images/')
    admin = models.ForeignKey(verbose_name='管理员id', to=Admin, to_field='id', on_delete=models.CASCADE, null=True)
