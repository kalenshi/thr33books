from django.db import models

from api.models.book import Book
from users.models import User


class Member(models.Model):
    """Model definition for application users"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = "member"
        app_label = "api"
