from django.db import models

# Create your models here.
class Voters(models.Model):
    boolChoice = (
        ("Male","Male"),("Female","Female")
    )
    statusChoice = (
        ("Yes","Yes"),("No","No")
    )
    #voterid, name, gender, age,place,status
    voterid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length = 6,choices=boolChoice)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    status = models.CharField(max_length = 3,choices=statusChoice)

    def __str__(self):
        return self.voterid + " " + self.name + " " + self.gender + " " 
        + self.age + " " + self.place + " " + self.status