from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('card/', include('card.urls')),
    path('line_bot/', include('line_bot.urls')),
]
