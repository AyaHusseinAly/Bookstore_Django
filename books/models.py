from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MinLengthValidator


class Category(models.Model):
    class Meta:
        verbose_name_plural="categories"
    
    name = models.CharField(max_length=50,validators=[MinLengthValidator(2)])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Isbn(models.Model):
    book_author= models.CharField(max_length=100,null=True)
    isbn_num = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Tag(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2048)
    author = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    isbn = models.OneToOneField(Isbn,null=True,blank=True, on_delete=models.CASCADE)
    tag= models.ForeignKey(Tag, null=True,blank=True, on_delete=models.CASCADE)

