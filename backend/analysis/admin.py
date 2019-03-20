from django.contrib import admin

from .models import AnalysisResponse


class AnalysisResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'tweet_id')

    def tweet_id(self, obj):
        return obj.tweet.id


admin.site.register(AnalysisResponse, AnalysisResponseAdmin)
