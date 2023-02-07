from django.shortcuts import render
from django.views.generic import ListView,FormView,CreateView
from .forms import PhotoForm
from .models import Photo
# Create your views here.


class UploadView(CreateView):
    template_name = 'website/index.html'
    form_class = PhotoForm
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gallery"] = Photo.objects.all()
        return context
