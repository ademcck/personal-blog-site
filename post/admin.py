from django.contrib import admin
from .models import Post , Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'pub_date', 'slug']
    date_hierarchy = 'pub_date' #yeni post 'dan eskiye sıralar
    list_filter = ['pub_date']
    list_display_links = ['pub_date'] #publis date link verildi
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(Category)