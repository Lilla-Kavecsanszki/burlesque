from django import forms
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from .models import Contact

class ContactForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('e.g., +39 333 123 4567'),
        })
    )

    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('John Doe'),
            }),
            "email": forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('example@site.com'),
            }),
            "subject": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('What would you like to discuss?'),
            }),
            "message": forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': _('Your message'),
            }),
        }
