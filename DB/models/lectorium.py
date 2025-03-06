from django.db import models


class Lectorium(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    location = models.IntegerField()
    size = models.IntegerField()
    type = models.IntegerField()
    equipment = [] # TODO DB (компьютеры, ничего и тд)
    description = models.CharField(max_length=300)
    organization = models.IntegerField()


    def get_id(self):
        return self.id

    def __str__(self):
        return (f"Lectorium (\n"
                f"number: {self.number}\n"
                f"location: {self.location},\n"
                f"size: {self.size},\n"
                f"type: {self.type},\n"
                f"equipment: {self.equipment}\n"
                f"description: {self.description}\n"
                f")")
