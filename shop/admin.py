from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Item, Comment,Category

class ItemAdmin(ModelAdmin):
    pass

admin.site.register(Item,ItemAdmin)

class CommentAdmin(ModelAdmin):
    pass

admin.site.register(Comment,CommentAdmin)

class CategoryAdmin(ModelAdmin):
    pass

admin.site.register(Category,CategoryAdmin)

