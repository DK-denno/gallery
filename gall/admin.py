from django.contrib import admin

# Register your models here.
from .models import Posts,Category,Location



class PostsAdmin(admin.ModelAdmin):
    filter_horizontal=('category','location')


admin.site.register(Posts,PostsAdmin)
admin.site.register(Category)
admin.site.register(Location)
