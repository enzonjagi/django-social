from django import forms
from .models import Dweet

class DweetForm(forms.ModelForm):
    """A Django form allowing users to create a Dweet"""

    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Salimia Watu ,pesa hupotea...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        """allows passing of any information
        that isn’t a field to the form class.
        """

        model = Dweet # The model it takes info from
        exclude = ("user", ) # Omits the 'user' field of the Dweet Model