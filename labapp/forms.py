from django import  forms
from labapp.models import Voters

class VotersForm(forms.ModelForm):
    class Meta:
        model = Voters
        fieldss = "__all__"