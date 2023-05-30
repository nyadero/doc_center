from django.contrib import admin

from .models import Category, Document

# Register your models here.
# register category model
admin.site.register(Category)
# register document model
admin.site.register(Document)
