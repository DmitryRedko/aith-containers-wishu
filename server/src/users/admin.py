from django.contrib import admin

from users.models import User, Friend


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ("user", "friend", )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined", 'birth_date')
