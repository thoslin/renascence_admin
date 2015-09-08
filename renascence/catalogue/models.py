from django.db import models
from category.models import CategoryFirstLevel, CategorySecondLevel


class Spu(models.Model):
    class Meta:
        db_table = "product"
        verbose_name = "SPU"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, null=True)
    sku_count = models.IntegerField()
    first_category = models.ForeignKey(CategoryFirstLevel, db_column="category_first_level_id")
    second_category = models.ForeignKey(CategorySecondLevel, db_column="category_second_level_id")

    def __unicode__(self):
        return u"%s" % self.name


class Sku(models.Model):
    class Meta:
        db_table = "item"
        verbose_name = "SKU"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    merchant_id = models.IntegerField(default=0)
    spu = models.ForeignKey(Spu, db_column="product_id")
    type = models.IntegerField(choices=((1, "for sell"), (2, "for rent")))
    total_count = models.IntegerField()
    current_count = models.IntegerField()
    price = models.FloatField()
    state = models.IntegerField(choices=((0, "off shelve"), (1, "shelve")))
    description = models.TextField(max_length=1024, null=True, blank=True)
    thumbnails = models.TextField(null=True, blank=True)
    pictures = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_column="shelf_time")

    def __unicode__(self):
        return "sku of [%s]" % self.spu.name