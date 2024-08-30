from django.db import models


class Book(models.Model):
    """The book model for the library"""
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    edition = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey("Member", on_delete=models.CASCADE)

    def __str__(self):
        """
        Human-readable representation of the book
        Returns:
            str : String representation of the book
        """
        return f"Book: {self.title}"

    class Meta:
        app_label = "api"
        db_table = "book"
