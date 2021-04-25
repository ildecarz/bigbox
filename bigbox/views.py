from django.shortcuts import render, get_object_or_404
from .models import Box, Activity
from django.views.generic import ListView, DetailView

#from django.core.paginator import Paginator
#from django.db.models import Count

# Create your views here.

class BoxListView(ListView):

    model = Box
    template_name = 'bigbox/boxes_list.html' 
    context_object_name = 'boxes'
    

class BoxDetailView(DetailView):

    model = Box
    template_name = 'bigbox/boxes_detail.html' 

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)
        context['activities'] = list(Activity.objects.values('name')[:5])
        return context

class ActivityListView(ListView):

    model = Activity
    template_name = 'bigbox/activity_list.html'
    context_object_name = 'activities'
    paginate_by = 20

class ActivityDetailView(DetailView):

    model = Activity
    template_name = 'bigbox/activity_detail.html'
    

class BoxSlugDetailView(DetailView):

    model = Box
    template_name = 'bigbox/boxes_detail.html'

  
    
