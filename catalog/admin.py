from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

admin.site.register(Genre)
# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAmdin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class bookInstncaeadmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
