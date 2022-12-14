from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Card
from django.urls import reverse_lazy

class ListCardView(ListView):
  template_name = 'card/card_list.html'
  model = Card

class CreateCardView(CreateView):
  template_name = 'card/card_create.html'
  model = Card
  fields = ("question", "answer_fake1", "answer_fake2","answer")
  success_url = reverse_lazy('list-card')

class DeleteCardView(DeleteView):
  template_name = 'card/card_confirm_delete.html'
  model = Card
  success_url = reverse_lazy('list-card')

class UpdateCardView(UpdateView):
  template_name = 'card/card_update.html'
  model = Card
  success_url = reverse_lazy('list-card')
  fields = ("question", "answer_fake1", "answer_fake2", "answer")

class DetailCardView(DetailView):
  template_name = 'card/card_detail.html'
  model = Card
  success_url = reverse_lazy('list-card')