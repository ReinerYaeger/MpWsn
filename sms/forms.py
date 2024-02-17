from django import forms
from .models import SensorCollectedData


class ChartDataForm(forms.Form):
    sensor_group_name = forms.ModelChoiceField(
        queryset=SensorCollectedData.objects.values_list('sensor_group_name', flat=True).distinct(),
        empty_label='Select Sensor Group'
    )
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
