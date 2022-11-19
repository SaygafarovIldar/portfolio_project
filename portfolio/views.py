from django.urls import reverse
import requests
from django.conf import settings
from django.shortcuts import HttpResponseRedirect, render, redirect

from . import forms
from . import models
from . import utils

telegram_settings = settings.TELEGRAM

chat_id = 5090318438

url = "https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"


def index_view(request):        
    testimonials = models.Recommendation.objects.all()
    resume_categories = models.ResumeCategory.objects.all()
    skills = models.Skill.objects.all()
    portfolio_items = models.PortfolioProject.objects.all()
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            full_name = form["full_name"].value()
            email = form["email"].value()
            message = form["message"].value()
            text = f"""
Имя отправителя: {full_name}
Почта отправителя: {email}
Сообщение: {message}            
"""
            requests.post(url.format(
                token=telegram_settings["bot_token"],
                chat_id=chat_id,
                text=text
            ))
            return HttpResponseRedirect(reverse('home'))
    else:
        form = forms.ContactForm()

    context = {
        "testimonials": testimonials,
        "resume_categories": resume_categories,
        "skills": skills,
        "portfolio_items": portfolio_items,
        "projects_types": utils.get_project_types(portfolio_items),
        "form": form
    }

    return render(request, "portfolio/index.html", context)
