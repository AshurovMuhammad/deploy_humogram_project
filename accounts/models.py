from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/avatars/', null=True, blank=True, verbose_name="Profil rasmi")
    birthday = models.DateField("Tug'ilgan sana", null=True)
    phone = models.CharField("Telefon raqam", max_length=13, null=True)
    following = models.ManyToManyField("self", blank=True, null=True, related_name="followers", symmetrical=False)

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    def __str__(self):
        return str(self.username)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def followers_count(self):
        count = self.followers.count()
        return count

    @property
    def following_count(self):
        return self.following.count()
