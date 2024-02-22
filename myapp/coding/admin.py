from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import PyCoding

# Register your models here.

admin.site.register(PyCoding, MarkdownxModelAdmin)