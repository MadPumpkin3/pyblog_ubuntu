from django.contrib import admin
from .models import PyBlog, PyBlogDetail

# Register your models here.
# @admin.register(PyBlog)
# class PyblogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'regist_dt', 'update_dt')
    
class containPythonBlog(admin.StackedInline):
    model = PyBlogDetail
    extra = 3
    
class admin_pythonblog(admin.ModelAdmin):
    list_display = ('id', 'title', 'regist_dt', 'update_dt')
    
    fieldsets = [
        (None, { 'fields': ['title'] }),
    ]
    inlines = [ containPythonBlog ]
    
admin.site.register(PyBlog, admin_pythonblog)
admin.site.register(PyBlogDetail)