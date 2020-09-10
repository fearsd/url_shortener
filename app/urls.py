from django.urls import path
from .views import URLViewSet

urlpatterns = [
    path('', URLViewSet.as_view({'post': 'create'})),
    path('<slug>', URLViewSet.as_view({'get': 'retrieve'}))
]