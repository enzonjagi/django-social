from django.shortcuts import render, redirect
from .models import Profile, Dweet
from .forms import DweetForm

# Create your views here.
def dashboard(request):
    """Renders the base.html template on the app's dashboard"""

    # Checks for a HTTP POST request to create a Dweet
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        # and then checks the validity of the form 
        # to then save the form input as a dweet, 
        # assigns the dweet to the user that sent the request, 
        # and save the dweet 
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")
        
    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    return render(
        request, 
        "dwitter/dashboard.html", 
        {"form": form, "dweets": followed_dweets}
    )

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
