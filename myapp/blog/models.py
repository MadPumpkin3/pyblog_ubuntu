from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.

class PyBlog(models.Model):
     id = models.AutoField(primary_key=True)
     title = models.CharField(max_length=100)
     update_dt = models.DateTimeField(auto_now=True)
     regist_dt = models.DateTimeField(auto_now_add=True)
     
     def get_absolute_url(self): # reverse 함수를 통해 모델의 개별 데이터 url를 문자열로 반환한다.
         return reverse("blog:blog_detail", kwargs={"pk": self.id})
    
     class Meta:
         db_table = 'py_blog'
        
class PyBlogDetail(models.Model):
     detail = models.ForeignKey(PyBlog, models.DO_NOTHING, related_name='pb_detail')
     sub_title = models.CharField(max_length=100, blank=True, null=True)
     img_url = models.CharField(max_length=200, blank=True, null=True)
     img_size = models.CharField(max_length=3, blank=True, null=True)
     content_body = models.TextField(blank=True, null=True)

     class Meta:
         managed = True
         db_table = 'py_blog_detail'
