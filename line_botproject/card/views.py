from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.core.exceptions import PermissionDenied
from .models import Card
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def index_view(request):
    object_list = Card.objects.order_by('category')
    return render(
        request,
        'card/index.html',
        {'object_list':object_list}
    )

class ListCardView(LoginRequiredMixin, ListView):
  template_name = 'card/list_card.html'
  model = Card

class CreateCardView(LoginRequiredMixin, CreateView):
  template_name = 'card/card_create.html'
  model = Card
  fields = ("question", "answer_fake1", "answer_fake2","answer", "category")
  success_url = reverse_lazy('list-card')
  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteCardView(LoginRequiredMixin, DeleteView):
  template_name = 'card/card_confirm_delete.html'
  model = Card
  success_url = reverse_lazy('list-card')
  # def get_object(self, queryset=None):
  #       obj = super().get_object(queryset)

  #       if obj.user != self.request.user:
  #           raise PermissionDenied

class UpdateCardView(LoginRequiredMixin, UpdateView):
  model = Card
  fields = ("question", "answer_fake1", "answer_fake2", "answer", "category")
  template_name = 'card/card_update.html'
  success_url = reverse_lazy('list-card')
  # def get_object(self, queryset=None):
  #   obj = super().get_object(queryset)
  #   if obj.user != self.request.user:
  #     raise PermissionDenied
  #     return obj
  # def get_success_url(self):
  #   # fields = ("question", "answer_fake1", "answer_fake2", "answer")
  #   return reverse('detail-card', kwarges={'pk': self.object.id})

class DetailCardView(LoginRequiredMixin, DetailView):
  template_name = 'card/card_detail.html'
  model = Card
  success_url = reverse_lazy('list-card')