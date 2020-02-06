from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200)
    # Comma separated category list.
    categories = models.CharField(max_length=100)
    description = models.TextField()
    solution = models.TextField()