from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .serializers import URLSerializer
from .models import URL
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin

# Create your views here.
class URLViewSet(viewsets.GenericViewSet, CreateModelMixin):
    serializer_class = URLSerializer
    def retrieve(self, request, slug):
        queryset = URL.objects.all()
        url = get_object_or_404(queryset, hash_slug=slug)
        return HttpResponseRedirect(url.exact_url)