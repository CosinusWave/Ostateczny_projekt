import datetime

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    library_card_number = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Shelf(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    shelf = models.ForeignKey(Shelf, on_delete=models.SET_NULL, null=True, blank=True)
    is_borrowed = models.BooleanField(default=False)
    borrowed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    borrowed_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.borrowed_by:
            self.borrowed_date = datetime.date.today()
            self.is_borrowed = True
        else:
            self.is_borrowed = False
            self.borrowed_date = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class DVD(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    release_date = models.DateField()
    shelf = models.ForeignKey(Shelf, on_delete=models.SET_NULL, null=True, blank=True)
    is_borrowed = models.BooleanField(default=False)
    borrowed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    borrowed_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.borrowed_by:
            self.borrowed_date = datetime.date.today()
            self.is_borrowed = True
        else:
            self.is_borrowed = False
            self.borrowed_date = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
