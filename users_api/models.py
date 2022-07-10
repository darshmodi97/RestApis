from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, URLValidator
# Create your models here.


class User(AbstractUser):
    company_name = models.CharField(max_length=200, blank=True, null=True,
                                    verbose_name="Company Name")

    age = models.PositiveIntegerField(
        verbose_name='Age',
        blank=True, null=True,
        validators=[MinValueValidator(1, message="Age can't be less than 1.")])

    city = models.CharField(max_length=50,
                            blank=True,
                            null=True,
                            verbose_name="City")

    state = models.CharField(max_length=50,
                            blank=True, null=True, verbose_name="State")

    zip = models.PositiveIntegerField(verbose_name="Zip", blank=True, null=True)
    web = models.URLField(verbose_name="Web",
                            validators=[URLValidator])

    email = models.EmailField(unique=True,
                              verbose_name="email address",
                              blank=True,
                              null=True)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
