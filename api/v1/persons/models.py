from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'persons'

    def __str__(self):
        return self.name
