from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from myapp.blog.models import PyBlog

class PythonBlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7
    
    def items(self):
        results = PyBlog.objects.all().order_by('-regist_dt')
        return results
    
    def location(self, obj):
        return """/blog/%s""" % obj.pk
    
    def lastmod(self, obj):
        return obj.update_dt