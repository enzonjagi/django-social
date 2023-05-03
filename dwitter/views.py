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

def profile(request, pk):
    """An individual view of each profile"""

    # Verify that the user has a profile 
    # if none we assign one to the user
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    # check for POST methods that request for: follow or unfollow actions
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(
        request,
        "dwitter/profile.html",
        {"profile": profile},
    )
