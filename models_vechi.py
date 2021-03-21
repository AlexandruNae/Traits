from django.db import models
from enum import Enum

class User(models.Model):
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    MALE = "M"
    FEMALE = "F"
    OTHER = "Other"
    SEX = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    ]
    sex = models.CharField(max_length=12, choices=SEX, default=MALE)
    parola = models.CharField(max_length=100,default='1234')

    def nume_prenume(self):
        return self.prenume + " " + self.nume

    # username = models.CharField(max_length=20, default='change_me')
    def __str__(self):
        return self.nume_prenume()


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=150)
    BINE = "GOOD"
    RAU = "BAD"
    G_B = [
        (BINE, "Good"),
        (RAU, "Bad"),
    ]
    good_bad = models.CharField(max_length=12, choices=G_B, default=BINE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster')
    # wall = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wall')

    def sa_nu_coincida(self):
        if self.user != self.wall:
            return True
        else:
            return False

    def __str__(self):
        return self.title