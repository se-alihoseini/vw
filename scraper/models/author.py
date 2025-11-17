from django.db import models
from base import BaseModel

class Author(BaseModel):
    name = models.CharField(max_length=100, null=False)
    birthdate = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=100, null=True)

    class Meta:
        app_label = "scraper"
