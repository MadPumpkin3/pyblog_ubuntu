from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('index.do', views.index.as_view(), name='main'),
    path('', views.firstIndex.as_view(), name='first_index'),
    path('blogs/', views.blogList.as_view(), name='pb_list'),
]
