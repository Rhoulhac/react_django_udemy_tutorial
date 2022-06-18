from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=36,
        blank=False,
        unique=True,
    )
    description = models.TextField(
        blank=True,
        max_length=256,
    )
    price = models.DecimalField(
        blank=True,
        decimal_places=2,
        max_digits=3,
        null=True,
    )
    published = models.DateField(
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(
        default=False,
    )
    cover = models.ImageField(
        blank=True,
        upload_to='covers/',
    )
