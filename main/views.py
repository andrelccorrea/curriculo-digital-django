from django.shortcuts import render
from django.contrib import messages
from django.views import generic

from .models import *
from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        certificates = Certificate.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context['certificates'] = certificates
        context['portfolio'] = portfolio

        return context


class ContactView(generic.FormView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'Obrigado. Entrarei em contato em breve.')
        return super().form_valid(form)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'main/portfolio-detail.html'
