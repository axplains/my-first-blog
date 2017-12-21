from django.contrib import admin

# Register your models here.

# importa il model "Post" creato in precedenza
from .models import Post
# lo aggiunge alla pagina di admin
admin.site.register(Post)
