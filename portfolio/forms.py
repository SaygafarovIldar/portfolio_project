from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "placeholder": "Full name",
        "class": "form-input",
        "data-form-input": ""
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Email address",
        "class": "form-input",
        "data-form-input": ""
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Your message",
        "class": "form-input",
        "data-form-input": "",
        "cols": "",
        "rows": "",
    }))
