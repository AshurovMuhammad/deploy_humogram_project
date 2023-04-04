from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/avatars/', null=True, blank=True, verbose_name="Profil rasmi")
    birthday = models.DateField("Tug'ilgan sana", null=True)
    phone = models.CharField("Telefon raqam", max_length=13, null=True)

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    def __str__(self):
        return str(self.username)
