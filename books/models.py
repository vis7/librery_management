from django.db import models
from django.urls import reverse
# from secound_app.models import YourModel

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=32)

class Book(models.Model): # pk
    name = models.CharField(max_length=32, help_text="enter name of book")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10) # models.IntegerField() # 
    is_available = models.BooleanField(default=True)
    pub_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='book_pic', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("books:book_detail_view", kwargs={"pk": self.pk})

class User(models.Model):
    name = models.CharField(max_length=32)
    mobile = models.IntegerField()
    books = models.ManyToManyField(Book, null=True, blank=True)
    num_books_take = models.IntegerField(default=0)

# djagno.contib.auth.models import User

# pip install Pillow

# class Genre():
#     name = 
#     Author = 

# chetalbhagt 


# 3 mistakes
# 2 states 
# half gf