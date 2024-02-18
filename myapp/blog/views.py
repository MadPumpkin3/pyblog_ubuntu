from django.shortcuts import render
from django.views import generic
from django.utils.functional import cached_property # 이건 뭐지?

from .models import PyBlog, PyBlogDetail

# Create your views here.

class sidebarMixin(object):
    @cached_property # 이건 뭐지 진짜?
    def getList(self):
        return PyBlog.objects.all
    
class firstIndex(generic.ListView):
    def __init__(self):
        self.title_nm = "PythonBlog에 오신것을 환영합니다."
        self.ogImgUrl = ""
        self.descript = ""
        self.template_name = "index.html"
        
    def get(self, request, *args, **kwargs):
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,
                        "dataList":"",
                        }
        return render(request, self.template_name, self.content)
    
class blogList(generic.ListView):
    model = PyBlog
    
class blogDetail(sidebarMixin, generic.View):
    def __init__(self):
        self.template_name = 'blog/blogDetail.html'
        
    def get_queryset(self):
        results = PyBlog.objects.filter(id=self.kwargs['pk'])
        results = results.values('id', 'title', 'update_dt', 'regist_dt', 
                                 'pb_detail__detail_id', 'pb_detail__sub_title', 
                                 'pb_detail__img_url', 'pb_detail__img_size', 'pb_detail__content_body')
        
        self.title_nm = results[0]['title']
        self.descript = results[0]['pb_detail__content_body'][:320]
        self.ogImgUrl = results[0]['pb_detail__img_url']
        return results
    
    def get(self, request, *args, **kwargs):
        self.content = {"dataList":self.get_queryset(),
                        "sidebarList":self.getList,
                        "descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,}
        
        return render(request, self.template_name, self.content)