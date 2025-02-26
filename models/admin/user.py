from django.contrib import admin
from models.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...
