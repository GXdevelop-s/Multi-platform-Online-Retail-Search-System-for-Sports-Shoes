from django.shortcuts import render, redirect

from app01 import models
from app01.utils import forms


# for admin only
def user_list(request):
    # 管理员有权限访问
    if request.session['info']['name'][0:6] == 'admin_':
        query_set = models.User.objects.all()
        return render(request, 'user_list.html', {'query_set': query_set})
    return render(request, 'no_right.html')


def user_add(request):
    title = '增加用户'
    if request.method == 'GET':
        form = forms.UserForm()
        return render(request, 'add.html', {'title': title, 'form': form})
    else:
        form = forms.UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/user/list/')
        return render(request, 'add.html', {'title': title, 'form': form})


def user_edit(request, nid):
    title = '用户编辑'
    if request.method == 'GET':
        user_obj = models.User.objects.filter(id=nid).first()
        form = forms.UserForm(instance=user_obj)
        return render(request, 'change.html', {'title': title, 'form': form})
    else:
        user_obj = models.User.objects.filter(id=nid).first()
        form = forms.UserForm(data=request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect('/admin/user/list/')
        return render(request, 'change.html', {'title': title, 'form': form})


def user_del(request, nid):
    models.User.objects.filter(id=nid).first().delete()
    return redirect('/admin/user/list/')
