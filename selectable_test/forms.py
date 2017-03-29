from django import forms
import selectable
from .models import Country
from .models import Machine
from .lookups import CityLookup
from .utils import trace


class MachineAdminForm(forms.ModelForm):
    city = selectable.forms.AutoCompleteSelectField(
        lookup_class=CityLookup,
        widget=selectable.forms.AutoComboboxSelectWidget,
        allow_new=False,
        required=False,
    )

    class Meta(object):
        model = Machine
        exclude = []
