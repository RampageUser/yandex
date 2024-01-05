from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'text', 'pub_date', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    list_editable = ('group',)
    empty_value_display = '-пусто-'


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
