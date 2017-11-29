from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug' : ('title',)} # slug 필드는 title 필드를 사용해 미리 채운다.


admin.site.register(Post, PostAdmin)