from django.shortcuts import render
from .models import Profile

# Create your views here.
def dashboard(request):
    """Renders the base.html template on the app's dashboard"""

    return render(request, "base.html")

def profile_list(request):
    """Creates a profile list from the Profiles created in the DB"""

    profiles = Profile.objects.exclude(user=request.user)
    return render(
        request,
        "dwitter/profile_list.html",
        {"profiles": profiles},
    )
