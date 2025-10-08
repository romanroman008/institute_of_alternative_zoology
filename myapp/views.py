from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import logging

from .models import Curiosity

from django.shortcuts import get_object_or_404


#@cache_page(60 * 15)
def index(request):
    logging.info("Fetching all curiosities from database")
    logging.info(f"User [{timezone.now().isoformat()}] {request.user} requested curiosties list from {request.META.get("REMOTE_ADDR")}")
    curiosities = Curiosity.objects.all()
    logging.debug(f"Found {curiosities.count()} curiosities")
    paginator = Paginator(curiosities, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, "myapp/index.html", context)


class IndexClassView(ListView):
    model = Curiosity
    template_name = "myapp/index.html"
    context_object_name = "curiosities"



class DetailsView(DetailView):
    model = Curiosity
    template_name = "myapp/details.html"
    context_object_name = "curiosity"

def details(request, id):
    logging.info(f"Fetching a curiosity with id {id}")
    logging.info(f"User [{timezone.now().isoformat()}] {request.user} requested curiosity with id {id}")
    try:
        curiosity = get_object_or_404(Curiosity, pk=id)
        logging.debug(f"Curiosity found: {curiosity}")
        context = {"curiosity": curiosity}
    except Exception as e:
        logging.error(f"Error fetching curiosity with id {id}: {e}")
        raise
    return render(request, "myapp/details.html", context)

class CuriosityCreateView(CreateView):
    model = Curiosity
    fields = ['topic', 'content', 'stupidity_scale']


class CuriosityUpdateView(UpdateView):
    model = Curiosity
    fields = ['topic', 'content', 'stupidity_scale']
    template_name_suffix = '_update_form'

class CuriosityDeleteView(DeleteView):
    model = Curiosity
    success_url = reverse_lazy('myapp:index')
