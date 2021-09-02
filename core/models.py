from django.db import models
from django.utils import timezone


class ModelWithAutoTimestamp(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if self._state.adding:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Scraper(ModelWithAutoTimestamp):
    name = models.TextField(null=True)
    url = models.TextField(null=True)
    price = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    image = models.TextField(null=True)
