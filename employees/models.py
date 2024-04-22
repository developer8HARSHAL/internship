from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    # Add other fields as needed

    class Meta:
        app_label = 'employees'
