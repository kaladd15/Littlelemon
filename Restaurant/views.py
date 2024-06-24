from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from .models import menu,booking
from .serializer import MenuSerializer, BookingSerializer

from rest_framework.permissions import IsAuthenticated

#@api_view()
@permission_classes([IsAuthenticated])

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer
class BookingView(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer