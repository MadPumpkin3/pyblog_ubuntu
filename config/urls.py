"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from config.sitemaps import PythonBlogSitemap

sitemaps = {
    'blog': PythonBlogSitemap,
}

urlpatterns = [
    # 검색엔진이 내 사이트 내에 있는 페이지들을 파악할 수 있게 sitemap을 만들어서 제공
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    # 검색엔진이 내 사이트를 수집할 때 제어할 수 있는 txt 파일 등록
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')), 
    path('admin/', admin.site.urls),
    path('', include('myapp.blog.urls')),
    path('', include('myapp.coding.urls')),
    # 마크다운 기능을 등록
    path('markdownx/', include('markdownx.urls')),
]

if settings.DEBUG:
   import debug_toolbar
   urlpatterns += [
       path('__debug__/', include(debug_toolbar.urls)),
   ]
