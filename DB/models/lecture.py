
from django.db import models


class Lecture(models.Model):


    def get_id(self):
        return self.id

    def __str__(self):
        return (f"Activity (\n"
                f"id: {self.id},\n"
                f"tutor: {self.tutor},\n"
                f"lectorium: {self.lectorium},\n"
                f"activity: {self.activity},\n" # TODO DB виды предметов
                f"start: {self.start},\n"
                f"end: {self.end}\n"
                f")")






