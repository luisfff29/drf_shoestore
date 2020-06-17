# from django.shortcuts import render
from shoe_store.models import Manufacturer, ShoeType, ShoeColor, Shoe
from rest_framework import viewsets
from api.serializers import (ManufacturerSerializer, ShoeTypeSerializer,
                             ShoeColorSerializer, ShoeSerializer)


# Create your views here.
class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
