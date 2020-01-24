from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import *
from django.views.generic.edit import CreateView
from .forms import *
from .models import Users
from django.urls import reverse_lazy


class ListView(ListView):
    model = Users
    template_name = 'core/lista.html'
    context_object_name = 'users'

class CRUD(CreateView):
    model = Users
    fields = '__all__'
    success_url = reverse_lazy('lista')