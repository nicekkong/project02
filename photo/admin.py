from __future__ import unicode_literals

from django.contrib import admin
from .models import Photo, Album


class PhotoInline(admin.StackedInline):
# class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 2


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [PhotoInline]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
