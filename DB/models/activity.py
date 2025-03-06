
from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=100)


    def get_id(self):
        return self.id

    def __str__(self):
        return f"Activity (name: {self.name})"






