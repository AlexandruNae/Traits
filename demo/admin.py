from django.contrib import admin
from .models import AuthUser as User, Post
# from .models import Book, BookNumber, Character, Author, User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['nume','prenume','username','parola','email','gender','descriere','data']
    # fields = "__all__"

admin.site.register(Post)