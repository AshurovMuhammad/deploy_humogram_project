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

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Follow(models.Model):
    to_user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)  # НА КОГО ПОДПИСАЛ
    from_user = models.ForeignKey(User, related_name="follows", on_delete=models.CASCADE)  # КТО ПОДПИСАЛ
    created = models.DateTimeField(auto_now_add=True)  # КОГДА ПОДПИСАЛ

    class Meta:
        verbose_name = "Obunachi"
        verbose_name_plural = "Obunachilar"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.from_user} obuna bo'lgan {self.to_user}ga"
