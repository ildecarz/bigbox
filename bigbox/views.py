from django.shortcuts import render
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

    def get(self, *args, **kwargs):
        pk1 = kwargs.get('pk', None)
        return super(BoxDetailView, self).get(*args, **kwargs)

class BoxActivityDetailView(DetailView):
    
    model = Activity
    template_name = 'bigbox/boxactivity_detail.html'
    context_object_name = 'activities'

    context = super().get_context_data(**kwargs)
    context['boxes'] = list(Box.objects.values('name')[:1])
    return context



class ActivityListView(ListView):

    model = Activity
    template_name = 'bigbox/activity_list.html'
    context_object_name = 'activities'
    paginate_by = 20


class ActivityDetailView(DetailView):

    model = Activity
    template_name = 'bigbox/boxes_detail.html'

    def get(self, *args, **kwargs):
        pk1 = kwargs.get('pk', None)
        pk2 = kwargs.get('pk2', None,)
        return super(ActivityDetailView, self).get(*args, **kwargs)
    
    

class BoxSlugDetailView(DetailView):

    model = Box
    template_name = 'bigbox/boxes_detail.html'

    def get_context_data(self, **kwargs):
    
        slug = super().get_context_data(**kwargs)
        slug['activities'] = list(Activity.objects.values('name')[:5])
        return slug

  
    
