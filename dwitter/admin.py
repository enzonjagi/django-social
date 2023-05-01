from django.contrib import admin
from django.contrib.auth.models import Group, User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """We use this to specify which fields 
    the Django admin should display
    """

    model = User
    # Limit the Django admin: to just dsiplay the username
    fields = ["username"]

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
