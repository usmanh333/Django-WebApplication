from abc import ABC
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import PostServices, Category
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


def post_services(request):
    context = {
        'posts': PostServices.objects.all()
    }
    return render(request, 'ubiquityOSI/post_services.html', context)


def list_of_post_by_category(request, category_slug=None):
    category = None
    categories = Category.objects.get(slug=category_slug)
    posts = PostServices.objects.filter(category__slug=category_slug)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
    template = 'ubiquityOSI/list_of_post_by_category.html'
    context = {'category': category, 'categories': categories, 'posts': posts}
    return render(request, template, context)


def home(request):
    context = {
        'posts': PostServices.objects.all()
    }
    return render(request, 'ubiquityOSI/home.html', context)


class HomeListView(ListView):
    model = PostServices
    template_name = 'ubiquityOSI/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class ServiceListView(ListView):
    model = PostServices
    template_name = 'ubiquityOSI/post_services.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


class UserServiceListView(ListView):
    model = PostServices
    template_name = 'ubiquityOSI/user_postservices.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PostServices.objects.filter(author=user).order_by('-date_posted')


class ServiceDetailView(DetailView):
    model = PostServices
    template_name = 'ubiquityOSI/postservices_detail.html'


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = PostServices
    fields = ['service_title', 'skills_description', 'enter_price', 'phone', 'location', 'area', 'category', 'select_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ABC):
    model = PostServices
    fields = ['service_title', 'skills_description', 'enter_price', 'phone', 'location', 'area', 'category', 'select_image']

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


def about(request):
    return render(request, 'ubiquityOSI/about.html', {'title': 'About'})
