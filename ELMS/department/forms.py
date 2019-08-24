from django import forms
from .models import DepartmentMaster

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentMaster
        fields = "__all__"
