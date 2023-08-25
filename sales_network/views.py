from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from sales_network.filters import CountryFilter
from sales_network.models import ChainLink
from sales_network.permissions import IsActiveUserPermission
from sales_network.serializators import ChainLinkSerializer, ChainLinkCreateSerializer


class ChainLinkCRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChainLink.objects.all()
    permission_classes = (IsActiveUserPermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CountryFilter
    serializer_class = ChainLinkSerializer

    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'PUT']:
            return ChainLinkCreateSerializer
        return ChainLinkSerializer


class ChainLinkListCreateView(generics.ListCreateAPIView):
    queryset = ChainLink.objects.all()
    permission_classes = (IsActiveUserPermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CountryFilter
    serializer_class = ChainLinkSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ChainLinkCreateSerializer
        return ChainLinkSerializer
