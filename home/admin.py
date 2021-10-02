from django.contrib import admin
from . models import Book, Category, Order

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'genre', 'author')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_id', 'user_id', 'name', 'orderedOn', 'address', 'amount')


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)