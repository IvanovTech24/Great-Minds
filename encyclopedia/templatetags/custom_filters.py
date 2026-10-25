from django import template

register = template.Library()

@register.filter
def get_lifespan(person):
    if person.death_year:
        return f"{person.birth_year} – {person.death_year}"
    return f"{person.birth_year} – Present"


@register.inclusion_tag('encyclopedia/partials/person_card.html')
def person_card(person):
    return {'person': person}