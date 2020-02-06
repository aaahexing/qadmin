from django.db import models


class Question(models.Model):
    class Level(models.IntegerChoices):
        EASY = 1
        MEDIUM = 2
        HARD = 3

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, default="engineer@pony.ai")
    # Comma separated category list.
    categories = models.CharField(max_length=100)
    level = models.IntegerField(choices=Level.choices, default=Level.EASY)
    description = models.TextField()
    solution = models.TextField()
    supplement = models.TextField(blank=True)
    # Comma separated external links.
    references = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title