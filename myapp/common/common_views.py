from django.utils.functional import cached_property
from myapp.blog.models import PyBlog, PyBlogDetail
from myapp.coding.models import PyCoding
import logging as log

class menuMixin(object):
    # @cached_property는 아래 매소드로 만든 메뉴 데이터를 실행할 때마다 db에서 가져오는 자원 낭비를 막기 위해 캐시하는 것으로 쓰인다.
    @cached_property
    def getMenuList(self):
        return {
            'blog_menu':PyBlog.objects.all(),
            'coding_menu':PyCoding.objects.all(),
            }