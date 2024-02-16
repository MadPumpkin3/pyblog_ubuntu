from django.shortcuts import render
from django.views import generic
from .models import PyBlog

# Create your views here.

# class index(generic.ListView):
#     def __init__(self):
#         self.title_nm = 'Pyblog'
#         self.ogImgUrl = ''
#         self.descript = '메인페이지입니다.'
#         self.template_name = 'blog/index.html'
        
#     def get(self, request, *args, **kwargs):
#         self.content = {
#             "descript": self.descript,
#             "title_nm": self.title_nm,
#             "ogImgUrl": self.ogImgUrl,
#             "dataList": PyBlog.objects.all(),
#         }
        
#         return render(request, self.template_name, self.content)
    
class firstIndex(generic.ListView):
    def __init__(self):
        self.title_nm = "PythonBlog에 오신것을 환영합니다."
        self.ogImgUrl = ''
        self.descript = ''
        self.template_name = 'index.html'
        
    def get(self, request, *args, **kwargs):
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,
                        "dataList":"",
                        }
        return render(request, self.template_name, self.content)
    
class blogList(generic.ListView):
    model = PyBlog