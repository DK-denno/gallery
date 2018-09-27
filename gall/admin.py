from django.contrib import admin

# Register your models here.
from .models import Posts,Category,Location


admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Location)
