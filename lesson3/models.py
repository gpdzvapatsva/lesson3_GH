from django.db import models

# Create your models here.
class Students(models.Model):
    firstname=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    student_id=models.IntegerField()
    course=models.CharField(max_length=30)

    def __str__(self):
        return (f"ID: {self.id} firstname {self.firstname},"
                f"surname {self.surname} Student ID {self.student_id},"
                f"Course : {self.course}")
