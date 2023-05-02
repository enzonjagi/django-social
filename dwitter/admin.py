from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Register your models here.
class ProfileInline(admin.StackedInline):
    """An inline Admin Profile registration
    
    Makes it easier to connect the User and Profile Models
    """

    model = Profile

class UserAdmin(admin.ModelAdmin):
    """We use this to specify which fields 
    the Django admin should display
    """

    model = User
    # Limit the Django admin: to just dsiplay the username
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
