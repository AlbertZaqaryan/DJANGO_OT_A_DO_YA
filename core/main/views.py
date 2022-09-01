from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        itemtype = ItemType.objects.all()
        return render(request, self.template_name, {'itemtype':itemtype})

class CategoryListView(ListView):
    template_name = 'home_detail.html'

    def get(self, request, id):
        category = ItemType.objects.filter(pk=id)
        return render(request, self.template_name, {'category':category})


class MarkListView(ListView):
    template_name = 'home_detail_detail.html'

    def get(self, request, id):
        mark = Category.objects.filter(pk=id)
        return render(request, self.template_name, {'mark':mark})


class ProductListView(ListView):
    template_name = 'product.html'

    def get(self, request, id):
        product = Mark.objects.filter(pk=id)
        return render(request, self.template_name, {'product':product})


class AboutDetailView(DetailView):
    template_name = 'about.html'

    def get(self, request, id):
        prod_about = Product.objects.get(pk=id)
        return render(request, self.template_name, {'prod_about':prod_about})

