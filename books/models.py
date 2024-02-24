from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(db_index=True, null=False, unique=True)
    cover = models.ImageField(upload_to="covers/", blank=True)

    class Meta:
        permissions = [("special_status", "Can read all books"), ]

    def __str__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save()


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review
