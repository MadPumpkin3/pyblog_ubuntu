from typing import Any
from django.shortcuts import render
from django.views import generic
from django.utils.functional import cached_property # 이건 뭐지?

from .models import PyBlog
import logging as log

# Create your views here.

class blogList(generic.ListView):
    model = PyBlog

class firstIndex(blogList, generic.ListView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_nm'] = 'django blog 클론코딩하기'
        context['ogImgUrl'] = ""
        context['descript'] = "현재 보고 계신 pyblog는 처음부터 끝까지 따라서 만들어본 블로그입니다."
        context['sidebarList'] = PyBlog.objects.all()
        return context

class blogDetail(blogList, generic.View):
    template_name = "blog/blogDetail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_set = PyBlog.objects.filter(id=self.kwargs['pk'], use_yn = 'Y')
        context['pageInfo'] = query_set[0]
        log.info(query_set.query)
        query_set = query_set.values('id', 'title', 'update_dt', 'regist_dt', 
                                 'pb_detail__detail_id', 'pb_detail__sub_title', 
                                 'pb_detail__img_url', 'pb_detail__img_size', 'pb_detail__content_body'
                                 ).order_by('pb_detail__sub_title')
        
        context['dataList'] = query_set
        context['title_nm'] = query_set[0]['title']
        context['descript'] = query_set[0]['pb_detail__content_body'][:320]
        context['ogImgUrl'] = query_set[0]['pb_detail__img_url']
        context['sidebarList'] = PyBlog.objects.all()
        return context