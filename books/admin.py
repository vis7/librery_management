from django.contrib import admin
from .models import Book, Author, Genre, User


class BookAdmin(admin.ModelAdmin):
    # fields = ['name', 'pub_date', 'price', 'is_available', 'genre', 'pic']
    fieldsets = [
        ("Basic Info", {'fields': ['name', 'price', 'pic']}),
        ("Publication Info", {'fields': ['pub_date', 'author', 'genre']})
    ]
    list_display = ['name', 'price', 'is_available', 'pub_date']
    search_fields = ['name', 'price']
    list_filter = ['pub_date']


class BookInline(admin.TabularInline):  # StackedInline
    model = Book
    extra = 3


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(User)
