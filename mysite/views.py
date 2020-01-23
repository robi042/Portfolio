import json
import requests
from django.shortcuts import render

from .models import Contact


def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        r = requests.get('http://api.icndb.com/jokes/random?firstName=' +firstname + '&lastName=' +lastname)
        json_data = json.loads(r.text)
        jokes = json_data.get('value').get('joke')
        context ={'joke': jokes}
        return render(request, 'mysite/index.html', context)

    else:
        firstname = 'Rabiul'
        lastname = 'Hasan'
        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        jokes = json_data.get('value').get('joke')
        context = {'joke': jokes}
        return render(request, 'mysite/index.html', context)


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        massage_r = request.POST.get('massage')

        c = Contact(email=email_r, subject=subject_r, massage=massage_r)
        c.save()

        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')


def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def details(request):
    return render(request, 'mysite/details.html')
