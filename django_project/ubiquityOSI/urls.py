from django.urls import path
from . import views
from .views import ServiceListView, ServiceCreateView, ServiceDetailView,\
    ServiceUpdateView, ServiceDeleteView, UserServiceListView, HomeListView


urlpatterns = [
    path('', HomeListView.as_view(), name='home-page'),
    path('services/post_services/<slug:category_slug>/', views.list_of_post_by_category, name='list_of_post_by_category'),
    path('user/<str:username>', UserServiceListView.as_view(), name='user-post-services'),
    path('services/', views.services, name='services-page'),
    path('about/', views.about, name='about'),
    path('post_services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('post_services/', ServiceListView.as_view(), name='post-services'),
    path('post_services/new/', ServiceCreateView.as_view(), name='create-post'),
    path('post_services/<int:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('post_services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
]


