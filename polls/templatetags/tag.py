from django import template
from polls.models import Contact

register = template.Library()

@register.simple_tag
def CvContains(contains=""):
    return Contact.objects.all().filter(message__contains=contains)
