from django.db import models

# Create your models here.
class contact(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
class upload_book(models.Model):
    ID = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="e_books/images",default="")
    detail = models.CharField(max_length=122)
    book = models.FileField(upload_to="e_books/books",default="")

    def __str__(self):
        return self.detail