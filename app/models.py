from django.db import models


# Create your models here.

class Doktor(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    telegramnikname = models.CharField(max_length=256)
    yonalishi = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.ism} {self.status}'


class Xamshira(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    telegramnikname = models.CharField(max_length=256)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.ism} {self.status}'


class Xona(models.Model):
    odam_soni = models.IntegerField(default=0)
    narxi = models.IntegerField("Narxi USD", default=0)

    def __str__(self):
        return f'{self.id}'


class Klient(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    phone = models.IntegerField()
    Xona = models.ForeignKey(Xona, on_delete=models.SET_NULL, null=True, blank=True)
    Doktor = models.ForeignKey(Doktor, on_delete=models.SET_NULL, null=True, blank=True)
    Xamshira = models.ForeignKey(Xamshira, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.ism}'
