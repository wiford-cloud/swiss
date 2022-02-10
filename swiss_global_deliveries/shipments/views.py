from dataclasses import fields
from multiprocessing import context
from pyexpat import model
from django.shortcuts import render
from django.views.generic import (
                                ListView,
                                DetailView,
                                CreateView
                                )
from .models import Client
# Create your views here.

class ClientListView(ListView):
    model = Client
    template_name="pages/home.html"
    cl_object_name = 'Client'

class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    template_name="pages/Client_create.html"
    fields = [
        'Name_of_item',
        'Supplier',
        'Description_notes',
        'Expected_Date_Delivery',
        'Status'
        ]

    def form_valid(self,form):
        form.instance.id = self.request.user
        return super().form_valid(form)

def home(request):

    cl = {
         'cl':Client.objects.all()
         }
    
    return render(request, "pages/home.html",cl)