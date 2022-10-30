
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Workers
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'data/index.html'
    context_object_name = 'latest_added_list'

    def get_queryset(self):
        """Return the last five workers added."""
        return Workers.objects.order_by('-name')[:5]

class DetailView(generic.DetailView):
    model = Workers
    template_name = 'data/detail.html'

class SalaryView(LoginRequiredMixin, generic.DetailView):
    permission_required = 'data.view_choice'
    model = Workers
    template_name = 'data/salary.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
def about(request):
    return render(request, 'data/about.html', {'title': 'About'})
    
     
    
    
    

    