from django.shortcuts import render, redirect
from .forms import *
from core.models import *
from django.contrib import messages


def homePage(request):
    starTreats = homeStarTreat.objects.all()

    return render(request, "home.html", {'starTreats': starTreats})


def contactPage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            memberMessages.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Your message has been sent successfully!')

            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})


def aboutPage(request):
    testimonials = Testimonial.objects.all()
    return render(request, "about.html", {'testimonials': testimonials})


def menuPage(request):
    items = MenuItem.objects.all()

    categories = {}
    for item in items:
        categories.setdefault(item.food_type, []).append(item)
    return render(request, "menu.html", {'categories': categories})