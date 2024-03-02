from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q

from app01 import models

from app01.utils import web_scraper
from app01.utils import forms


# 商品推荐先行页
def recom_transition(request):
    if request.method == 'GET':
        return render(request, 'recommend_transition.html')


# pre推荐页
def pre_recom(request):
    if request.method == 'GET':
        dict_url = {
            'url': '/recom/recommend/'
        }
        return JsonResponse(dict_url)


# 显示推荐页
def recom_show(request):
    user_id = request.session['info']['id']
    row_obj = models.RecomKey.objects.filter(user=user_id).first()
    if request.method == 'GET':
        form = forms.KeyForm()
        return render(request, 'recommend.html', {'form': form})
    else:
        form = forms.KeyForm(data=request.POST, instance=row_obj)
        if form.is_valid():
            user_instance = models.User.objects.get(id=user_id)
            if row_obj:
                # 如果已存在实例，更新其他字段并保存
                row_obj.key1 = form.cleaned_data['key1']
                row_obj.key2 = form.cleaned_data['key2']
                row_obj.key3 = form.cleaned_data['key3']
                # ... 更新其他字段
                row_obj.save()
            else:
                form.save()
            return redirect('/recom/recommend/result/')
        return render(request, 'recommend.html', {'form': form})


# 推荐结果
def recom_res(request):
    key_obj = models.RecomKey.objects.filter(user=request.session['info']['id']).first()
    # 拼接关键字
    keyword = key_obj.band + key_obj.get_key1_display() + key_obj.get_key2_display() + key_obj.get_key3_display()
    commodity_scraper = web_scraper.CommodityScraper(keyword)
    link_list, commodity_list, price_list = commodity_scraper.do_scraper()  # 爬取商品信息并返回

    # 按照元组装包
    datalist = []
    for i in range(len(link_list)):
        datalist.append((link_list[i], commodity_list[i], price_list[i]))
    # 按照既定规则排序
    if key_obj.get_key3_display() == '低价':
        sorted_data_list = sorted(datalist, key=lambda x: float(x[2]))
    elif key_obj.get_key3_display() == '高级':
        sorted_data_list = sorted(datalist, key=lambda x: float(x[2]), reverse=True)
    else:
        sorted_data_list = datalist
    return render(request, 'recom_res.html', {'datalist': sorted_data_list})


# pre排行选择页
def pre_ranking_choice(request):
    if request.method == 'GET':
        dict_url = {
            'url': '/recom/ranking_choice/'
        }
        return JsonResponse(dict_url)


# 显示排行选择页
def ranking_choice_show(request):
    if request.method == 'GET':
        # 查询 跑鞋、徒步鞋、足球鞋、篮球鞋
        query_set1 = models.ShoeProduct.objects.filter(Q(type=1035) | Q(type=9914) | Q(type=1032) | Q(type=1034))
        # 查询 羽毛球鞋、轮滑鞋、综合训练鞋、舞蹈鞋
        query_set2 = models.ShoeProduct.objects.filter(Q(type=5853) | Q(type=10106) | Q(type=10304) | Q(type=1033))
        # 查询 高尔夫球鞋、运动凉鞋
        query_set3 = models.ShoeProduct.objects.filter(Q(type=7429) | Q(type=9906))
        # 封装成列表
        query_set_list = [query_set1, query_set2, query_set3]
        return render(request, 'ranking_choice.html', {'query_set_list': query_set_list})


# 排行榜
def rank(request, nid):
    if request.method == 'GET':
        obj = models.ShoeProduct.objects.filter(type=nid).first()
        website = obj.rank_link
        # 拿到type对应的排行榜网址，实例化爬虫
        scraper = web_scraper.RankScraper(website)
        # 爬取数据
        result_dict = scraper.do_scraper()
        top10_rank = result_dict['band_list']
        top10_description = result_dict['band_description_list']
        print(len(top10_rank))
        print(len(top10_description))
        rank_list = []  # 以元组为元素的列表
        # 只要前十,并按照元组来对应[(排名,品牌,描述),(排名,品牌,描述).....]
        for i in range(0, 10):
            rank_list.append((i + 1, top10_rank[i], top10_description[i]))
        # 修改用户last_choice
        models.User.objects.filter(name=request.session['info']['name']).update(last_choice=nid)
        return render(request, 'rank_all.html', {'rank_list': rank_list})
