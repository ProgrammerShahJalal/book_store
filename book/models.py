from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
    CATEGORY = (
        ('Fiction', 'Fiction'),
        ("Non-fiction", "Non Fiction"),
        ('Si-Fi', 'Si-Fi'),
        ('Horor', 'Horor'),
        ('Romance', 'Romance'),
        ('Thriller', 'Thriller'),
        ('Mystery', 'Mystery'),
        ('History', 'History'),
        ('Biography','Biography'),
        ('Cookbook','Cookbook'),
        ('Traveler','Traveler'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField( max_length=30)
    author = models.CharField(max_length = 30)
    category = models.CharField(max_length = 30, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add = True)
    last_pub = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"Book Name-{self.book_name} Author-{self.author}"
    