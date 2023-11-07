from django.shortcuts import render
from rest_framework import generics
from catalog.models import Perfum
from catalog.serializers import PerfumSerializer


class PerfumAPI(generics.ListAPIView):
    queryset = Perfum.objects.all()
    serializer_class = PerfumSerializer
