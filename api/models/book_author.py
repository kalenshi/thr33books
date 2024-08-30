from django.db import models

from api.models.author import Author
from api.models.book import Book


class BookAuthor(models.Model):
    """Model for linking each book to an author"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    def __str__(self):
        """Return string representation of book author"""
        return f"{self.book} - {self.author}"

    class Meta:
        unique_together = (("book", "author"),)
        app_label = "api"
        db_table = "book_author"
