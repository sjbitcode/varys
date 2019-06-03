from django.contrib import admin

from .models import Author, Tweet


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'handle')


class TweetAdmin(admin.ModelAdmin):
    list_display = ('id', '_text')

    def _text(self, obj):
        return str(obj)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tweet, TweetAdmin)
