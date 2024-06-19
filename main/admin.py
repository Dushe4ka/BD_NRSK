from django.contrib import admin
from main.models import Author, Book
# Register your models here.


@admin.register(Author)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)


@admin.register(Book)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("id", "title", "author", "public_year")
