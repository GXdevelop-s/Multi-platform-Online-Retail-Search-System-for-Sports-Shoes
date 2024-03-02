from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from app01 import models
from app01.utils import forms


# 用户注册前一步
def pre_register(request):
    dict_url = {
        'url': 'register/'
    }
    return JsonResponse(dict_url)


# 用户注册
def register(request):
    if request.method == 'GET':
        form = forms.UserSignupForm()
        print('fuck')
        return render(request, 'register.html', {'form': form})
    else:
        form = forms.UserSignupForm(request.POST)
        if form.is_valid():
            # 表单验证通过，执行保存等操作
            form.save()
            return redirect('/login/')  # 重定向到成功页面
    # 表单验证不通过
    return render(request, 'register.html', {'form': form})


# 用户/管理员登录
def login(request):
    if request.method == 'GET':
        form = forms.LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            # 管理员登录
            if form.cleaned_data.get('username')[0:6] == 'admin_':
                admin_obj = models.Admin.objects.filter(admin_name=form.cleaned_data.get('username'),
                                                        password=form.cleaned_data.get('password')).first()
                # 登录失败
                if not admin_obj:
                    form.add_error('password', '用户名或密码错误')
                    # 用户名或者密码错误，返回
                    return render(request, 'login.html', {'form': form})
                else:
                    # 登录成功，设置session
                    request.session['info'] = {'id': admin_obj.id, 'name': admin_obj.admin_name}
                    request.session.set_expiry(60 * 60 * 24 * 1)  # 有效期一天                                       
                    return redirect('/index/')
            else:
                # 用户登录
                user_obj = models.User.objects.filter(name=form.cleaned_data.get('username'),
                                                      password=form.cleaned_data.get('password')).first()
                if not user_obj:
                    form.add_error('password', '用户名或密码错误')
                    return render(request, 'login.html', {'form': form})
                else:
                    request.session['info'] = {'id': user_obj.id, 'name': user_obj.name}
                    request.session.set_expiry(60 * 60 * 24 * 1)  # 有效期一天
                    return redirect('/index/')


# 广告加载
def index_ad():
    ad_obj = models.Advertisement.objects.latest('id')
    return ad_obj


# 首页
def index(request):
    # 只处理用户的首页显示
    if request.session['info']['name'][0:6] != 'admin_':
        user_id = request.session['info']['id']
        user_obj = models.User.objects.filter(id=user_id).first()
        # 查询上一次用户的搜索类型
        index_key = user_obj.last_choice
        product_obj = models.ShoeProduct.objects.filter(type=index_key).first()
        # 广告查询
        ad_obj = index_ad()
        # product_dict = {
        #     'picture1': models.ShoeProduct.objects.filter(type=index_key).first().picture1,
        #     'picture2': models.ShoeProduct.objects.filter(type=index_key).first().picture2,
        #     'picture3': models.ShoeProduct.objects.filter(type=index_key).first().picture3,
        #     'description1': models.ShoeProduct.objects.filter(type=index_key).first().details1,
        #     'description2': models.ShoeProduct.objects.filter(type=index_key).first().details2,
        #     'description3': models.ShoeProduct.objects.filter(type=index_key).first().details3,
        # }
        return render(request, 'index.html', {'product_obj': product_obj, 'ad_obj': ad_obj})
    else:  # 管理员进入
        product_obj = models.ShoeProduct.objects.filter(type=1035).first()
        # 广告查询
        ad_obj = index_ad()
        # product_dict = {
        #     'picture1': models.ShoeProduct.objects.filter(type=1035).first().picture1,
        #     'picture2': models.ShoeProduct.objects.filter(type=1035).first().picture2,
        #     'picture3': models.ShoeProduct.objects.filter(type=1035).first().picture3,
        #     # 管理员怎么进入都是跑鞋
        #     'description': models.ShoeProduct.objects.filter(type=1035).first().details1,
        #     'description2': models.ShoeProduct.objects.filter(type=1035).first().details2,
        #     'description3': models.ShoeProduct.objects.filter(type=1035).first().details3,
        # }
        return render(request, 'index.html', {'product_obj': product_obj, 'ad_obj': ad_obj})


# 登出
def logout(request):
    request.session.clear()
    return redirect('/login/')
