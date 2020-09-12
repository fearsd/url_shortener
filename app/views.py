from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin

from .serializers import URLSerializer
from .models import URL


class URLViewSet(viewsets.GenericViewSet):
    serializer_class = URLSerializer
    def retrieve(self, request, slug):
        queryset = URL.objects.all()
        url = get_object_or_404(queryset, hash_slug=slug)
        return HttpResponseRedirect(url.exact_url)

    def create(self, request):
        _serializer = self.get_serializer(data=request.data)
        if _serializer.is_valid():
            url, _ = URL.objects.get_or_create(exact_url=_serializer.data['exact_url'])
        else:
            return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = URLSerializer(url)
        return Response(serializer.data, status=status.HTTP_201_CREATED)