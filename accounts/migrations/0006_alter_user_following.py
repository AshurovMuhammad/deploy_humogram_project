# Generated by Django 3.2.9 on 2023-04-06 03:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20230406_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
