from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import logging

from .forms import CommentForm
from .models import Curiosity

from django.shortcuts import get_object_or_404


#@cache_page(60 * 15)
def index(request):
    logging.info("Fetching all curiosities from database")
    logging.info(f"User [{timezone.now().isoformat()}] {request.user} requested curiosties list from {request.META.get("REMOTE_ADDR")}")
    curiosities = Curiosity.objects.all()
    logging.debug(f"Found {curiosities.count()} curiosities")
    paginator = Paginator(curiosities, 6)
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
        if request.method == "POST":
            form = CommentForm(data=request.POST)
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.curiosity = curiosity
            new_comment.save()
            messages.success(request, "Dodano komentarz.")
            url = reverse("myapp:details", args=[curiosity.id])
            return redirect(f"{url}#comment-{new_comment.id}")
        comment_form = CommentForm()
        context = {"curiosity": curiosity, "comment_form": comment_form}
    except Exception as e:
        logging.error(f"Error fetching curiosity with id {id}: {e}")
        raise
    return render(request, "myapp/details.html", context)

