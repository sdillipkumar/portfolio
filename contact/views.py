from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from django.shortcuts import redirect
# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Compose the email
            subject = f"New Contact Form Submission from {name}"
            full_message = f"Sender Name: {name}\nSender Email: {email}\n\nMessage:\n{message}"

            try:
                send_mail(
                    subject,
                    full_message,
                    settings.EMAIL_HOST_USER,         # From Email
                    [settings.EMAIL_HOST_USER],       # To Email (your Gmail)
                    fail_silently=False,
                )
                messages.success(request, "Thank you! Your message has been sent successfully.")
                return redirect('home')  # Replace with your desired redirect
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})