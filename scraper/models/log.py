from django.db import models
from base import BaseModel


class Log(BaseModel):
    hash = models.CharField(max_length=1000, null=False)

    class Meta:
        app_label = "scraper"
