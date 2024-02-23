from django.contrib import admin
from markdownx.widgets import AdminMarkdownxWidget
from markdownx.admin import MarkdownxModelAdmin
from markdownx.models import MarkdownxField

from .models import PyCoding
from treebeard.forms import movenodeform_factory
from treebeard.admin import TreeAdmin

# Register your models here.

class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(PyCoding)

admin.site.register(PyCoding, CategoryAdmin)