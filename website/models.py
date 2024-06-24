from django.db import models
from django.core.validators import RegexValidator


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r"^\+?1?\d{9,15}$", "Enter a valid phone number.")],
    )
    address = models.TextField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(r"^\d{5}(?:[-\s]\d{4})?$", "Enter a valid zipcode.")
        ],
    )

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
