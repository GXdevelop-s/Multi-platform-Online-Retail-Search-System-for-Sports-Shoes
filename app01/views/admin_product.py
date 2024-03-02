from django.shortcuts import render, redirect

from app01 import models
from app01.utils import forms


# for admin only
def product_list(request):
    # 管理员有权限访问
    if request.session['info']['name'][0:6] == 'admin_':
        query_set = models.ShoeProduct.objects.all()
        return render(request, 'product_list.html', {'query_set': query_set})
    # 用户无权访问
    return render(request, 'no_right.html')


def product_add(request):
    title = '添加产品类'
    if request == 'GET':
        form = forms.ProductForm()
        return render(request, 'add.html', {'form': form, 'title': title})
    form = forms.ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/admin/product/list')
    else:
        return render(request, 'add.html', {'form': form, 'title': title})


def product_edit(request, nid):
    title = '编辑产品类'
    if request.method == 'GET':
        product_obj = models.ShoeProduct.objects.filter(id=nid).first()
        form = forms.ProductForm(instance=product_obj)
        return render(request, 'change.html', {'title': title, 'form': form})
    else:
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin/product/list/')
        return render(request, 'change.html', {'title': title, 'form': form})


def product_del(request, nid):
    product_exist = models.ShoeProduct.objects.filter(id=nid).exists()
    if product_exist:
        models.ShoeProduct.objects.filter(id=nid).delete()
        return redirect('/admin/product/list/')
