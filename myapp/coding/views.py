from django.shortcuts import render
from django.views import generic
from .models import PyCoding

from myapp.common.common_views import menuMixin

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