from django.db import models


class CategoryFirstLevel(models.Model):
    class Meta:
        db_table = "category_first_level"
        verbose_name = "Primary Category"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return u"%s" % self.name


class CategorySecondLevel(models.Model):
    class Meta:
        db_table = "category_second_level"
        verbose_name = "Secondary Category"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    first_level = models.ForeignKey(CategoryFirstLevel)

    def __unicode__(self):
        return u"%s -> %s" % (self.first_level.name, self.name)


class CategoryThirdLevel(models.Model):
    class Meta:
        db_table = "category_third_level"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    second_level = models.ForeignKey(CategorySecondLevel)

    def __unicode__(self):
        return u"%s" % self.name
