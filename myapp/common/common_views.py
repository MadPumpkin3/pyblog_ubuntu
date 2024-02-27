from django.shortcuts import render
from django.utils.functional import cached_property
from myapp.blog.models import PyBlog, PyBlogDetail
from myapp.coding.models import PyCoding
import logging as log

from django.views import generic

class menuMixin(object):
    # @cached_property는 아래 매소드로 만든 메뉴 데이터를 실행할 때마다 db에서 가져오는 자원 낭비를 막기 위해 캐시하는 것으로 쓰인다.
    @cached_property
    def getMenuList(self):
        return {
            'blog_menu':PyBlog.objects.all(),
            'coding_menu':PyCoding.objects.all(),
            }
        
class customHandler404(generic.View):
    def get(self, request, *args, **kwargs):
        context = menuMixin().getMenuList
        return render(request, "errors/404.html", context)
    
def handler500(request):
    context = menuMixin().getMenuList
    response = render(request, "errors/500.html", context=context)
    response.status_code = 500
    return response

class TagMixin(object):
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(tags__icontains=q)
        return queryset