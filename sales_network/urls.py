from django.urls import path

from sales_network.views import ChainLinkCRUDView, ChainLinkListCreateView

app_name = 'chainlink'

urlpatterns = [
    path('<int:pk>', ChainLinkCRUDView.as_view(), name='chainlinkCRUD'),
    path('', ChainLinkListCreateView.as_view(), name='chainlink_list'),
]

