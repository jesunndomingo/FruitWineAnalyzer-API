from django.contrib import admin
from .models import update_table, history_table
# Register your models here.

admin.site.register(update_table)
admin.site.register(history_table)