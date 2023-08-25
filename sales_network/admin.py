from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from sales_network.models import Contacts, Products, ChainLink


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_date')


@admin.register(ChainLink)
class ChainLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'supplier_url', 'debt',)
    actions = ('set_dead_to_zero',)
    list_filter = ['contact__city']

    @staticmethod
    def supplier_url(obj: ChainLink) -> str | None:
        if obj.supplier:
            return format_html('<a href="{}">{}</a>',
                               reverse('admin:sales_chain_chainlink_change', args=[obj.supplier_id]),
                               obj.supplier,
                               )

    @admin.action(description='Clear debt')
    def set_dead_to_zero(self, queryset):
        queryset.update(debt=0)
