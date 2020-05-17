from django.contrib import admin
from .models import Post

# register post model to admin area
admin.site.register(Post)
