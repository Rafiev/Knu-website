from django.db import models

class Applicant(models.Model):
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    grade = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.name 