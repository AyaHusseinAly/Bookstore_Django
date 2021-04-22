from django.contrib import admin
from .models import Book , Isbn ,Category, User, Tag
from .forms import BookForm


class BookInline(admin.StackedInline):
    model = Book
    max_num =3
    extra =1

class TagAdmin(admin.ModelAdmin):
    inlines= [BookInline]


class BookAdmin(admin.ModelAdmin):
    form=BookForm
    search_fields=("title",)
    list_filter=("categories",)
    list_display=("title",)
    #readonly_fields =("isbn","author")

class CategoryAdmin(admin.ModelAdmin):
    list_display=("name",)

class IsbnAdmin(admin.ModelAdmin):
    list_display=("book_author","isbn_num")



# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Isbn,IsbnAdmin)
admin.site.register(Category,CategoryAdmin)