from datetime import date
from django.forms import ModelForm, DateInput, TimeInput, NumberInput
from django.core.exceptions import ValidationError

from .models import Meeting


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start': TimeInput(attrs={"type": "time"}),
            'duration': NumberInput(attrs={"type": "number", "min": "1", "max": "4"}),
        }
    
    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d and d < date.today():
            raise ValidationError("Meetings cannot be in the past")
        return d
