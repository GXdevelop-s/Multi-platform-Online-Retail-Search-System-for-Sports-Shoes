from django import forms
from django.core.exceptions import ValidationError

from app01 import models
from app01.utils import bootstrap
from app01.utils.encrypt import md5


# 用户/管理员 登录通用表单
class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput,
        required=True,  # 必填不可为空

    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(render_value=True),
        required=True
    )

    def clean_username(self):
        name = self.cleaned_data.get('username')
        if len(name) < 3:
            raise ValidationError('无效用户名')
        return name

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)


# 管理员表单
class AdminForm(bootstrap.BootstrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['admin_name', 'password']
        # 本身自带的密码用这个
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    def clean_admin_name(self):
        name = self.cleaned_data.get('admin_name')
        if name[0:5] != 'admin':
            raise ValidationError('请注意，管理员账号名必须以admin_开头,_为英文下滑线')
        return name

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm_pwd = md5(self.cleaned_data.get('confirm_password'))
        # 比较md5加密之后的值
        if pwd != confirm_pwd:
            raise ValidationError('两次输入的密码不一致')  # 密码不一致抛出异常
        return confirm_pwd  # 密码一致，将确认的密码返回到表单中了，若此时form.save(),也是能保存


# 管理员注册表单
class AdminSignupForm(bootstrap.BootstrapModelForm):
    # 确认密码
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)  # 密码不一致也不会清空了
    )

    class Meta:
        model = models.Admin
        fields = ['admin_name', 'password']
        # 本身自带的密码用这个
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    def clean_admin_name(self):
        name = self.cleaned_data.get('admin_name')
        if name[0:5] != 'admin':
            raise ValidationError('请注意，管理员账号名必须以admin_开头,_为英文下滑线')
        return name

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm_pwd = md5(self.cleaned_data.get('confirm_password'))
        # 比较md5加密之后的值
        if pwd != confirm_pwd:
            raise ValidationError('两次输入的密码不一致')  # 密码不一致抛出异常
        return confirm_pwd  # 密码一致，将确认的密码返回到表单中了，若此时form.save(),也是能保存


# 用户注册表单
class UserSignupForm(bootstrap.BootstrapModelForm):
    # 确认密码
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)  # 密码不一致也不会清空了
    )

    class Meta:
        model = models.User
        fields = ['name', 'age', 'occupation', 'gender', 'password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        if len(self.cleaned_data.get('password')) < 6:
            raise ValidationError('密码至少为6位数')
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm_pwd = md5(self.cleaned_data.get('confirm_password'))
        # 比较md5加密之后的值
        if pwd and confirm_pwd and pwd != confirm_pwd:
            raise ValidationError('两次输入的密码不一致')  # 密码不一致抛出异常
        return confirm_pwd  # 密码一致，将确认的密码返回到表单中了，若此时form.save(),也是能保存


# product表单
class ProductForm(bootstrap.BootstrapModelForm):
    class Meta:
        model = models.ShoeProduct
        exclude = ['admin']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['picture1'].widget.attrs['input_type'] = 'file'
        self.fields['picture2'].widget.attrs['input_type'] = 'file'
        self.fields['picture3'].widget.attrs['input_type'] = 'file'


# 用户表单
class UserForm(bootstrap.BootstrapModelForm):
    class Meta:
        model = models.User
        exclude = ['admin']


# 推荐关键字表单
class KeyForm(bootstrap.BootstrapModelForm):
    class Meta:
        model = models.RecomKey
        fields = ['key1', 'key2', 'key3', 'band']

    # 设置字段必填
    def __init__(self, *args, **kwargs):
        super(KeyForm, self).__init__(*args, **kwargs)
        self.fields['key1'].required = True  # 将字段设置为必填项
        self.fields['key2'].required = True
        self.fields['key3'].required = True


# 广告表
class AdvertisementForm(bootstrap.BootstrapModelForm):
    class Meta:
        model = models.Advertisement
        exclude = ['admin']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ad_picture'].widget.attrs['input_type'] = 'file'
