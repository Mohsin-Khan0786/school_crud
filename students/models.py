from django.db import models

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  
    REQUIRED_FIELDS = [] 
    def __str__(self):
        return self.email
    
class Student(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.user.email}"
