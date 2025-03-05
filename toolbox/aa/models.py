from django.db import models

class Course(models.Model):  # ต้องเป็น models.Model
    Course_id = models.CharField(max_length=100, primary_key=True)
    Course_name = models.CharField(max_length=100)
    Teacher = models.CharField(max_length=100)
