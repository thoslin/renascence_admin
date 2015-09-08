from django.contrib import admin

# Register your models here.
from .models import CategoryFirstLevel, CategorySecondLevel


class CategoryFirstLevelAdmin(admin.ModelAdmin):
    pass


class CategorySecondLevelAdmin(admin.ModelAdmin):
    pass


admin.site.register(CategoryFirstLevel, CategoryFirstLevelAdmin)
admin.site.register(CategorySecondLevel, CategorySecondLevelAdmin)
