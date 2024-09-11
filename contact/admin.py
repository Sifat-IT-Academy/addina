from django.contrib import admin
from contact.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user','short_message']
    search_fields = ['user', 'message']

    def short_message(self,obj):
        return obj.message[:20]+'...'
