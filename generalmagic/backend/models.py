from django.db import models


class Registration(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Only store the hashed password

    class Meta:
        unique_together = ('email',)

    def __str__(self):
        return f"{self.fullname} ({self.email})"