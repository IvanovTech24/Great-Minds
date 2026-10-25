from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from encyclopedia.models import Person, Quote, Era
from gallery.models import Work
import random


def home(request: HttpRequest) -> HttpResponse:
    people_count = Person.objects.count()
    if people_count > 3:
        featured_people = random.sample(list(Person.objects.all()), 3)
    else:
        featured_people = Person.objects.all()

    quotes = Quote.objects.all()
    quote_of_the_day = random.choice(quotes) if quotes else None

    stats = {
        'people_count': Person.objects.count(),
        'works_count': Work.objects.count(),
        'eras_count': Era.objects.count(),
    }

    context = {
        'featured_people': featured_people,
        'quote_of_the_day': quote_of_the_day,
        'stats': stats,
    }

    return render(request, 'core/home-page.html', context)