from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class CategoryInventory(models.Model):
    __tablename__ = "category"
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = "category"

    def __str__(self):
        return self.category
