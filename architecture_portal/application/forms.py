from django import forms

from application.models import Application


class PriceCalculatorForm(forms.Form):
    square_meters = forms.FloatField(label='Total Area (sqm)', min_value=10)
    floors = forms.IntegerField(label='Number of Floors', min_value=1)
    design_complexity = forms.ChoiceField(
        label='Design Complexity',
        choices=[
            ('simple', 'Simple'),
            ('medium', 'Medium'),
            ('complex', 'Complex')
        ],
        widget=forms.RadioSelect
    )
    additional_services = forms.MultipleChoiceField(
        label='Additional Services',
        choices=[
            ('3d', '3D Visualization'),
            ('interior', 'Interior Design'),
            ('permit', 'Permit Assistance'),
            ('construction', 'Construction Supervision')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'client_name',
            'client_email',
            'client_phone',
            'project_title',
            'project_type',
            'project_description'
        ]
        widgets = {
            'project_description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Describe your project in detail (minimum 20 characters)'
            }),
            'project_type': forms.Select(attrs={'class': 'form-select'})
        }
