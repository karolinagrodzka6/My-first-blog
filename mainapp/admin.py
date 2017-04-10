from django.contrib import admin
from .models import Post, User, comment


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "published_date", "created_date"]
    list_display_links = ["created_date"]
    list_editable = ["title"]
    list_filter = ["published_date", "created_date"]

    search_fields = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
admin.site.register(User)
admin.site.register(comment)



