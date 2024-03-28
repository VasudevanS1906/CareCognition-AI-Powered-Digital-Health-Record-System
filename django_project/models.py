from django.db import models


class Health(models.Model):
    patient_id = models.CharField(max_length=100, unique=True)
    patient_name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=255)
    reason_for_visit = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.patient_name