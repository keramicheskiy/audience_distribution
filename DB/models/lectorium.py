from django.db import models


class Lectorium(models.Model):
    number = models.IntegerField() # номер аудитории с буквами
    location = models.CharField(max_length=100) # TODO DB номер/название корпуса
    size = models.IntegerField()
    type = models.IntegerField() # ENUM (Аудитория, комната для пз и тд)
    equipment = [] # TODO DB (компьютеры, ничего и тд)
    description = models.CharField(max_length=300)


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
