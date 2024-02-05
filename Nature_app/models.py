from django.db import models


class Nature(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
