from django.shortcuts import render

from django.db import models
from .forms import ContactForm, ContactBuyForm, SearchForm
from .models import Mebel, Category
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class ServicesPageView(TemplateView):
    template_name = 'services.html'

class ListProductView(ListView):
    model = Mebel
    template_name = 'shop.html'


class DetailPageView(DetailView):
    model = Mebel
    template_name = 'detail_product.html'

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            # print(f"Ism: {name}, tel: {phone}, Xabar: {message}")
            return render(request, 'contact_success.html', {'name': name})

        else:
            return render(request, 'contact.html', {'form': form})

    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})


def get_category(request, fstr):
    try:
        category = Category.objects.get(cat_name=fstr)
        posts = Mebel.objects.filter(categoty=category)
        # print(posts)
        return render(request, 'category.html', {'posts':posts})

    except:
        return render(request, 'services.html', {})

def contact_buy(request, pk):
    form = ContactBuyForm(initial={'key': f"Maxsulot ID = {pk}"})
    if request.method == 'POST':
        form = ContactBuyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            # print(f"Key: {pk}, Ism: {name}, tel: {phone}, Xabar: {message}")
            return render(request, 'contact_success.html', {'name': name, 'pk': pk})
        else:
            return render(request, 'buy.html', {'form': form})
    else:
        return render(request, 'buy.html', {'form': form})


def search_view(request):
    query = request.GET.get('query', '')
    posts = []

    if query:
        posts = Mebel.objects.filter(
            models.Q(title__icontains=query) | models.Q(pk__icontains=query) | models.Q(material__icontains=query)
        )

    return render(request, 'search.html', {'form': SearchForm(), 'posts': posts, 'query': query})