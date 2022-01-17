from dataclasses import fields
from django import forms
from .models import Plan


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['title']

        labels = {'title': ''}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Enter your plan here...'
            })
