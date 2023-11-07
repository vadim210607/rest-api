from django.db import models


class Perfum(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True)
    bottle = models.ForeignKey('Bottle', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Bottle(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type
