from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomepageView(TemplateView):
    template_name = "pages/index.html"


class Kitchen(TemplateView):
    template_name = "pages/kitchen.html"


class Bedroom(TemplateView):
    template_name = "pages/bedroom.html"

class Office(TemplateView):
    template_name = "pages/office.html"

class Furniture(TemplateView):
    template_name = "pages/furniture.html"


class Door(TemplateView):
    template_name = "pages/door.html"


class Decoration(TemplateView):
    template_name = "pages/decoration.html"

class Contact(TemplateView):
    template_name = "pages/contact.html"
