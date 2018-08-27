from django.shortcuts import render
from django.views.generic import View
import json
from django_redis import get_redis_connection


# Create your views here.
class InfoView(View):
    """购物车数据信息"""

    def get(self, request):
        """主页面"""

        return render(request, "index.html", {"text": "erwa"})
