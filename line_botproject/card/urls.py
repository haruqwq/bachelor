from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='list-card'),
    path('card/', views.ListCardView.as_view(), name='index'),
    path('card/<int:pk>/detail', views.DetailCardView.as_view(), name='detail-card'),
    path('card/create/', views.CreateCardView.as_view(), name='create-card'),
    path('card/<int:pk>/delete', views.DeleteCardView.as_view(), name='delete-card'),
    path('card/<int:pk>/update', views.UpdateCardView.as_view(), name='update-card'),
    ]