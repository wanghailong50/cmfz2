import re

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from cmfz.settings import PERMISSION_LIST


class CheckPermission(MiddlewareMixin):
    """
    用户权限信息的校验
    """

    def process_request(self, request):
        """
        当用户发起访问请求时先执行此中间件
        :param request:  当前用户要访问的url   用户的session权限列表
        :return:  是否有权访问
        """

        current_url = request.path_info
        print(current_url)

        per_list = request.session.get(PERMISSION_LIST)

        #
        # # 设置路径白名单
        valid_url_list = [
            "/login/page/",
            "/login/verify/",
            "/admin/.*",    # 以admin开头的全部路径都放行
            '/postman/first_page/',
            '/favicon.ico',
            '/'


        ]
        # # 用户当前要访问的url是否在白名单中  在不拦截
        for url in valid_url_list:
            if re.match(url, current_url):
                return None
        #
        # # 判断用户是否有权限访问
        for url in per_list:
            # 使用正则完成验证
            if current_url == url:
                return None

        return HttpResponse("无权访问")
