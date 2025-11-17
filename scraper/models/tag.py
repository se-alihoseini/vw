from django.db import models
from base import BaseModel
from scraper.models import Author


class Tag(BaseModel):
    content = models.CharField(max_length=30, null=False)

    class Meta:
        app_label = "scraper"
