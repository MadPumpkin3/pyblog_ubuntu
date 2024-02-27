from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import PyCoding

from myapp.common.common_views import menuMixin, TagMixin

# Create your views here.

class codingDetail(menuMixin, generic.DetailView):
    model = PyCoding
    
    def get_context_data(self, **kwargs):
        context = super(codingDetail, self).get_context_data(**kwargs)
        queryset = PyCoding.objects.get(id=self.kwargs['pk'])
        context['pageInfo'] = queryset
        context['blog_menu'] = self.getMenuList['blog_menu']
        context['coding_menu'] = self.getMenuList['coding_menu']
        return context
    
class TagListView(TagMixin, menuMixin, generic.ListView):
    model = PyCoding
    template_name = "coding/tags.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = super().get_queryset().filter(depth=2)
        context['q'] = self.request.GET.get("q")
        context.update(self.getMenuList)
        return context