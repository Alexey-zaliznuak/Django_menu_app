from django.contrib import admin
from .models import Resource, Menu


class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'url',
        'parent',
    )
    search_fields = ('parent', 'url', 'pk')
    list_filter = ('parent',)
    list_editable = ('parent', 'url')
    empty_value_display = '-пусто-'


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    list_editable = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Menu, MenuAdmin)
admin.site.register(Resource, ResourceAdmin)
