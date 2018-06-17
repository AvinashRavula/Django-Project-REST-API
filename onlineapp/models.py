from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    acronym = models.CharField(max_length=8)
    contact = models.EmailField()

    def __str__(self):
        return self.acronym


class Student(models.Model):
    name = models.CharField(max_length=128)
    dob = models.DateField(null=True,blank=True)
    email = models.EmailField()
    dropped_out = models.BooleanField(default=False)
    # college_name = models.CharField(max_length=64)
    db_folder = models.CharField(max_length=64)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name + " score was -> "+str(self.total)


class Mocktest1(models.Model):
    problem1 = models.IntegerField()
    problem2 = models.IntegerField()
    problem3 = models.IntegerField()
    problem4 = models.IntegerField()
    total = models.IntegerField()
    student = models.OneToOneField(Student,on_delete=models.CASCADE)

    def __str__(self):
        return "Student (self.student.name) marks"



from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
