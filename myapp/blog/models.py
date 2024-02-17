from django.db import models

# Create your models here.

# class PyBlog(models.Model):
#     id = models.AutoField(primary_key=True, null=False)
#     title = models.CharField(max_length=100)
#     update_dt = models.DateTimeField(auto_now=True)
#     regist_dt = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         db_table = 'py_blog'
        
# class PyBlogDetail(models.Model):
#     detail = models.ForeignKey(PyBlog, models.DO_NOTHING, related_name='pb_detail')
#     sub_title = models.CharField(max_length=100, blank=True, null=True)
#     img_url = models.CharField(max_length=200, blank=True, null=True)
#     img_size = models.CharField(max_length=3, blank=True, null=True)
#     content_body = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'py_blog_detail'