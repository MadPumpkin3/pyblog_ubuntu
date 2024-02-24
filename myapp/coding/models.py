from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from treebeard.mp_tree import MP_Node
from django.utils.functional import cached_property

# Create your models here.

IMG_SIZE_CHOICES = [(30, '30%'), (40, '40%'), (50, '50%'), (70, '70%'), (100, '100%')]

class PyCoding(MP_Node):
    id = models.AutoField(primary_key=True)
    tags = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    img_url = models.CharField(max_length=200, blank=True, null=True)
    img_size = models.IntegerField(choices=IMG_SIZE_CHOICES, blank=False, null=False)
    # content_body = models.TextField(null=False, blank=False)
    content_body = MarkdownxField()
    update_dt = models.DateTimeField(auto_now=True)
    regist_dt = models.DateTimeField(auto_now_add=False)
    
    node_order_by = ['regist_dt']
    
    def get_absolute_url(self):
        if not self.is_root():
            return reverse("coding:coding_detail", kwargs={"pk": self.pk})
    
    @cached_property
    def get_previous(self):
        if not self.is_root():
            return self.get_prev_sibling()
    
    @cached_property
    def get_next(self):
        if not self.is_root():
            return self.get_next_sibling()
        
    def get_is_root(self):
        return self.is_root()
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'py_coding'
        # ordering = ['regist_dt']