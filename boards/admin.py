from django.contrib import admin

# Register your models here.
from boards.models import Post, Bid

admin.site.register(Post)
admin.site.register(Bid)