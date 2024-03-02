from django.shortcuts import render, redirect

from app01 import models
from app01.utils import forms


def ad_add(request):
    if request.method == 'GET':
        form = forms.AdvertisementForm()
        return render(request, 'add.html', {'form': form})
    else:
        form = forms.AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # 重定向到首页
            return redirect('/index/')
        return render(request, 'add.html', {'form': form})
