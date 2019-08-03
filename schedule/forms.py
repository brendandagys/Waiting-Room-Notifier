from django import forms
from schedule.models import Schedule

MODALITY_CHOICES = (
    ('Unspecified', 'Unspecified'),
    ('Do Not Contact', 'Do Not Contact'),
    ('Phone', 'Phone'),
    ('Email', 'Email'),
    ('Phone & Email', 'Phone & Email'),
)

class ScheduleForm(forms.Form):

    slot = forms.CharField(label='Timeslot', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Timeslot...'}))
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Name...'}))
    modality = forms.ChoiceField(label='Contact Method', choices=MODALITY_CHOICES)
    phone = forms.CharField(label='Phone #', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Phone Number...'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Email Address...'}))
    status = forms.CharField(label='Status', disabled=True, initial='Not Ready', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Status...'}))

    def clean_slot(self):
        return self.cleaned_data['slot']

    def clean_name(self):
        return self.cleaned_data['name']

    def clean_modality(self):
        return self.cleaned_data['modality']

    def clean_phone(self):
        return self.cleaned_data['phone']

    def clean_email(self):
        return self.cleaned_data['email']

    def clean_status(self):
        return self.cleaned_data['status']
