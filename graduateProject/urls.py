"""
URL configuration for graduateProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app01.views import accounts, admin_product, admin_user, recommend, advertisement

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 登录/登出/注册/首页
    path('pre/register/', accounts.pre_register),
    path('register/', accounts.register),
    path('login/', accounts.login),
    path('index/', accounts.index),
    path('logout/', accounts.logout),

    # 产品管理
    path('admin/product/list/', admin_product.product_list),
    path('admin/product/add/', admin_product.product_add),
    path('admin/product/<int:nid>/edit/', admin_product.product_edit),
    path('admin/product/<int:nid>/del/', admin_product.product_del),

    # 用户管理
    path('admin/user/list/', admin_user.user_list),
    path('admin/user/add/', admin_user.user_add),
    path('admin/user/<int:nid>/edit/', admin_user.user_edit),
    path('admin/user/<int:nid>/del/', admin_user.user_del),

    # 产品推荐部分
    path('recom/transition/', recommend.recom_transition),
    path('recom/pre/recommend/', recommend.pre_recom),
    path('recom/recommend/', recommend.recom_show),
    path('recom/pre/ranking_choice/', recommend.pre_ranking_choice),
    path('recom/ranking_choice/', recommend.ranking_choice_show),
    # 排行
    path('recom/<int:nid>/ranking/', recommend.rank),  # 要带typeid来才能判断显示谁的榜单
    # 推荐结果
    path('recom/recommend/result/', recommend.recom_res),

    # 广告
    path('ad/add/', advertisement.ad_add)
]
# 通常，这个URL模式只在开发环境中使用，因此在条件语句中添加一个if settings.DEBUG的判断：

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 代码的作用是将MEDIA_URL下的媒体文件映射到MEDIA_ROOT目录中的实际文件。
# 确保将以上代码放置在URL配置文件的最后，以确保它们在其他URL模式之后被匹配。
