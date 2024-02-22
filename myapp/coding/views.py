from django.shortcuts import render
from django.views import generic
from .models import PyCoding

# Create your views here.

class codingDetail(generic.DetailView):
    model = PyCoding
    context_object_name = 'pageInfo'