from django.contrib import admin
from .models import Post, Category, Region, Cultivation, Alertlevel

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Cultivation)
admin.site.register(Alertlevel)