from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


# 如果中间件中没有返回值，则继续向后走，若是有返回值httpresponse render redirect，则不再向后执行
# 中间件实现用户登录校验
class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        # 0.排除那些不需要登录就能访问的页面
        if request.path_info == '/login/' or request.path_info == '/pre/register/' or request.path_info == '/register/':
            return
        # 1.读取当前访问用户的session信息，如果能读到，说明已经登录过，就可以继续向后走
        info_dict = request.session.get('info')
        if info_dict:
            return
        # 2.未登录过,回到登录页面
        return redirect('/login/')
