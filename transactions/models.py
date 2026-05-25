from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class IssueBook(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE)

    issue_date = models.DateField(auto_now_add=True)

    due_date = models.DateField()

    returned = models.BooleanField(default=False)