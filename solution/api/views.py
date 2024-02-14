from rest_framework import generics

from solution.api.permissions import *
from solution.api.serializers import *
from solution.models import Quote


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('-id')
    serializer_class = QuotesSerializer
    permission_classes = [IsAdminOrReadOnly]


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuotesSerializer
    permission_classes = [IsAdminOrReadOnly]