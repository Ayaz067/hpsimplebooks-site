from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def project(request):
    return render(request, 'main/project.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            send_mail(
                f'New Message from {name}',
                message, email, [settings.DEFAULT_FROM_EMAIL],
            )
            return render(request, 'main/contact.html', {'form': ContactForm,'success': True})
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def why_choose_us(request):
    return render(request, 'main/why_choose_us.html')

def our_services(request):
    return render(request, 'main/our_services.html')


def new_client_questionnaire(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        return render(request, 'main/new_client_questionnaire.html', {"submitted": True})

    return render(request, 'main/new_client_questionnaire.html')