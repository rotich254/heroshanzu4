from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
