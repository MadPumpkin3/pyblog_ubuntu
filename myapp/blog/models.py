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
     
     def get_previous(self): # regist_dt 기준으로 이전 객체를 가져오는 코드
         return self.get_previous_by_regist_dt()
     
     def get_next(self): # regist_dt 기준으로 다음 객체를 가져오는 코드
         return self.get_next_by_regist_dt()
    
     class Meta:
         db_table = 'py_blog'
        
class PyBlogDetail(models.Model):
     detail = models.ForeignKey(PyBlog, models.DO_NOTHING, related_name='pb_detail')
     sub_title = models.CharField(max_length=100, blank=True, null=True)
     img_url = models.CharField(max_length=200, blank=True, null=True)
     img_size = models.CharField(max_length=3, blank=True, null=True)
     content_body = models.TextField(blank=True, null=True)
    # 아래는 관리자 페이지에서 마크업 작업과 예시를 보여주기 위한 코드임(사용하려면 null에 대한 데이터 입력이 수동으로 필요함.)
    #  content_body = MarkdownxField()

     class Meta:
         managed = True
         db_table = 'py_blog_detail'
