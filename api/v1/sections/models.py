from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'sections'

    def __str__(self):
        return self.name
