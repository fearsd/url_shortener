from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin

from .serializers import URLSerializer
from .models import URL


class URLViewSet(viewsets.GenericViewSet, CreateModelMixin):
    serializer_class = URLSerializer
    def retrieve(self, request, slug):
        queryset = URL.objects.all()
        url = get_object_or_404(queryset, hash_slug=slug)
        return HttpResponseRedirect(url.exact_url)