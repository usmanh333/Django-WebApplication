from abc import ABC
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import PostServices
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'ubiquityOSI/home.html')


class ServiceListView(ListView):
    model = PostServices
    template_name = 'ubiquityOSI/post_services.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class UserServiceListView(ListView):
    model = PostServices
    template_name = 'ubiquityOSI/user_postservices.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PostServices.objects.filter(author=user).order_by('-date_posted')


class ServiceDetailView(DetailView):
    model = PostServices


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = PostServices
    fields = ['title', 'description_content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ABC):
    model = PostServices
    fields = ['title', 'description_content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostServices
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def services(request):
    return render(request, 'ubiquityOSI/services.html', {'title': 'Services'})


def services_providers(request):
    return render(request, 'ubiquityOSI/services_providers.html', {'title': 'Services Providers'})


def post_services(request):
    context = {
        'posts': PostServices.objects.all()
    }
    return render(request, 'ubiquityOSI/post_services.html', context)

