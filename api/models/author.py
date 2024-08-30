from django.db import models


class Author(models.Model):
    """The author of the book"""
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        """String representation of the author"""
        return f"Author: {self.first_name}, {self.last_name}"

    class Meta:
        app_label = "api"
        db_table = "author"
