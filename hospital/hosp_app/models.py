from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class ConsultTime(models.Model):
    time = models.CharField(max_length=2000)

    def __str__(self):
        return self.time


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    qualification = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    consulting_time = models.ManyToManyField(ConsultTime)
    image = models.ImageField(upload_to='doctor_image', default='doc.jpeg', blank=True)

    def __str__(self):
        return self.name

class Patient(models.Model):

    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=50)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.full_name





