from django.contrib import admin

from .models import Book, BookNumber, Character, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['published']


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)