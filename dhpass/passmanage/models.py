from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
# python manage.py makemigrations passmanage
# python manage.py migrate
