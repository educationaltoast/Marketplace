from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView, DetailView
from .models import Category,  Item, ItemForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Item

    template_name = "shop/home.html"

# class CreateItemFormView(FormView):
#     template_name = "shop/createForm.html"
#
#     form_class = ItemForm
#
#
#     def form_valid(self, request, form):
#         form = ItemForm(request.POST)
#         item = form.save()
#         item.save()
#         return super().form_valid(form)
#
#

class ItemCreateView(CreateView):
    model = Item
    template_name = 'shop/createForm.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class ItemDetailView(DetailView):
    model = Item
    template_name = "shop/itemDetail.html"
    fields = "__all__"
