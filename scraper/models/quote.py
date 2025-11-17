from django.db import models
from base import BaseModel


class Quote(BaseModel):
    content = models.TextField(null=False)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name="quotes")
    tag = models.ManyToManyField('Tag', blank=True, related_name="quotes")

    class Meta:
        app_label = "scraper"
