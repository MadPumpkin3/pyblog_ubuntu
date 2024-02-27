from django.urls import path
from . import views

app_name = 'coding'

urlpatterns = [
    path('coding/<int:pk>/', views.codingDetail.as_view(), name='coding_detail'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
]
