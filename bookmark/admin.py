from django.contrib import admin
from bookmark.models import Bookmark, Gm_Bookmark

# Register your models here.

class BookMarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


class GmBookMarkAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Bookmark, BookMarkAdmin)
admin.site.register(Gm_Bookmark, GmBookMarkAdmin)
