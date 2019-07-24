from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from voluntary.models import Activity

# Create your views here.


class ListActivities(ListView):
    model = Activity
    template_name = 'voluntary/detail.html'


class IndexView(TemplateView):
    template_name = 'voluntary/index.html'
