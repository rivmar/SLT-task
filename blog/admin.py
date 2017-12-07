from django.contrib import admin
from .models import Category, Record

class RecordAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Record, RecordAdmin)
admin.site.register(Category, CategoryAdmin)

