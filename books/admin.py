from django.contrib import admin
from .models import Book, Review
# Register your models here.


class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline,]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "price",)


admin.site.register(Book, BookAdmin)
admin.site.register(Review)
