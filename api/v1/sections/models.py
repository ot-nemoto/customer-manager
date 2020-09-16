from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
