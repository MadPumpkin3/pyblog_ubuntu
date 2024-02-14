from django.urls import path
from . import views

urlpatterns = [
    path('index.do', views.index.as_view(), name='main'),
    path('', views.firstIndex.as_view(), name='first_index'),
]
