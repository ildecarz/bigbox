from django.urls import path
from .views import BoxListView, BoxDetailView, ActivityListView, ActivityDetailView, BoxSlugDetailView

urlpatterns = [
    path('base_url/box/', BoxListView.as_view(), name='box-list-view'),
    path('base_url/box/<int:pk>/', BoxDetailView.as_view(), name='box-detail-view'),
    path('base_url/box/<int:pk>/activity/', ActivityListView.as_view(), name='activity-list-view'),
    path('base_url/box/<int:pk>/activity/<int:pk>', ActivityDetailView.as_view(), name='activity-detail-view'),
    path('base_url/box/<slug>', BoxSlugDetailView.as_view(), name= 'slug-view')
]
