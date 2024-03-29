from django.urls import path

from solution.api.views import *

urlpatterns = [
    path('quotes/', QuoteListCreateAPIView.as_view(), name='quote-list'),
    path('quotes/<int:pk>/', QuoteDetailAPIView.as_view(), name='quote-detail'),
]
