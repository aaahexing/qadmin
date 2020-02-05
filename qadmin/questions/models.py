from django.db import models


class Question(models.Model):
    CHOICES = (
        (11, 'Algorithm'),
        (12, 'Data Structure'),
        (13, 'Trick'),
        (14, 'Programming'),
        (15, 'Games'),
        (21, 'Operatiing System'),
        (32, 'Control Theory'),
    )

    title = models.CharField(max_length=200)
    categories = models.IntegerField(choices=CHOICES, default=11)
    description = models.TextField()
    solution = models.TextField()