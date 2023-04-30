from django.contrib import admin
from notes import models


class NotesAdmin(admin.ModelAdmin):
    # list_display = ['']
    # list_filter = ['']
    # search_fields = ['']
    pass


class CategoriesAdmin(admin.ModelAdmin):
    # list_display = ['']
    # list_filter = ['']
    # search_fields = ['']
    pass


admin.site.register(models.Notes, NotesAdmin)
admin.site.register(models.Categories, CategoriesAdmin)
