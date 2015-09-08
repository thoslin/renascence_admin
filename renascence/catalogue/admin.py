from django.contrib import admin
from catalogue.models import Spu, Sku


class SkuInline(admin.StackedInline):
    model = Sku
    exclude = ('merchant_id',)
    extra = 1


class SpuAdmin(admin.ModelAdmin):
    inlines = [SkuInline]


class SkuAdmin(admin.ModelAdmin):
    exclude = ('merchant_id',)

admin.site.register(Spu, SpuAdmin)
admin.site.register(Sku, SkuAdmin)
