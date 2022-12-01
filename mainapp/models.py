from django.db import models

# Create your models here.
class Sertificate(models.Model):
    nomer = models.CharField(max_length=200)
    url = models.TextField(blank=True, null=True)
    ism_familiya = models.CharField(max_length=200)
    kurs_nomi = models.TextField()
    kurs_soati = models.IntegerField()
    upload_link = models.TextField(default="media/pdf/")
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomer