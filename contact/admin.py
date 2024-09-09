from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user__username','user__phone_number','short_message')
    search_fields = ('user__username', 'message')

    def short_message(self,obj):
        return obj.message[:20]+'...'
