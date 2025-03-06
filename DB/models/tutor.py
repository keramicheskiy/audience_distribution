from django.db import models

class Tutor(models.Model):


    def __str__(self):
        return (f"Tutor (\n"
                f"id: {self.id},\n"
                f"name: {f"{self.tutor.lastname} {self.tutor.firstname[0]}. {self.tutor.patronymic[0]}."},\n"
                f"phone_number: {self.phone_number},\n"
                f"email: {self.email},\n"
                f"sex: {self.sex},\n"
                f"disciplines: {self.disciplines},\n" # список предметов у препода.
                f"organization: {self.organization},\n"
                f"faculty: {self.faculty}"
                f")")