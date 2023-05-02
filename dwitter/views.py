from django.shortcuts import render

# Create your views here.
def dashboard(request):
    """Renders the base.html template on the app's dashboard"""

    return render(request, "base.html")
