from django import forms
from .models import InspectionReport

class InspectionReportForm(forms.ModelForm):
    class Meta:
        model = InspectionReport
        fields = ('title', 'description')
