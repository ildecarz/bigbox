from django.shortcuts import render
from .models import Box, Activity
from django.views.generic import ListView, DetailView
from django.conf import settings

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
    # paginate_by = 20
    paginate_by = settings.PAGE_SIZE_ILD


class BoxActivityDetailView(DetailView):

    model = Activity
    template_name = 'bigbox/activity_detail.html'
    context_object_name = 'activities'  

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['page_alt']= Box.objects.get(id=self.kwargs.get('pk_1'))
        return context

class BoxSlugDetailView(DetailView):

    model = Box
    template_name = 'bigbox/boxes_detail.html'

    def get_context_data(self, **kwargs):
    
        slug = super().get_context_data(**kwargs)
        slug['activities'] = list(Activity.objects.values('name')[:5])
        return slug

  
    
