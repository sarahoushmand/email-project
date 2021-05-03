from django.contrib import admin
from .models import Email, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date')


admin.site.register(Email)
admin.site.register(Message, MessageAdmin)
