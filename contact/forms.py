# contact/forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'w-full p-3 rounded-lg bg-white/10 text-white backdrop-blur placeholder:text-white/60',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full p-3 rounded-lg bg-white/10 text-white backdrop-blur placeholder:text-white/60',
        'placeholder': 'Your Email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full p-3 rounded-lg bg-white/10 text-white backdrop-blur placeholder:text-white/60',
        'placeholder': 'Your Message',
        'rows': 5
    }))
