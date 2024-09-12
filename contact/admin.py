from django.contrib import admin
from contact.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'phone', 'birthday', 'short_message']
    search_fields = ['name', 'email', 'phone']

    def short_message(self,obj):
        return obj.message[:20]+'...'
