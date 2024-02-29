from django.contrib import admin
from .models import PyBlog, PyBlogDetail
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
from markdownx.models import MarkdownxField

# Register your models here.
# @admin.register(PyBlog)
# class PyblogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'regist_dt', 'update_dt')
    
class containPythonBlog(admin.StackedInline):
    model = PyBlogDetail
    extra = 3
    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget}
    }
    
class admin_pythonblog(admin.ModelAdmin):
    list_display = ('id', 'title', 'use_yn', 'regist_dt', 'update_dt')
    
    fieldsets = [
        (None, { 'fields': ['title', 'use_yn'] }),
    ]
    inlines = [ containPythonBlog ]
    
    # class Media:
    #     js = ('admin/js/markdown_preview.js',)
    
admin.site.register(PyBlog, admin_pythonblog)
admin.site.register(PyBlogDetail, MarkdownxModelAdmin)