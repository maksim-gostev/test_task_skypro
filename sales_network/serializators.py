from rest_framework import serializers

from sales_network.models import Contacts, Products, ChainLink


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('title',)


class SecondSupplierSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    @staticmethod
    def get_type(obj: ChainLink) -> str:
        return obj.get_type_display()

    class Meta:
        model = ChainLink
        fields = ('id', 'title', 'type',)


class SupplierSerializer(SecondSupplierSerializer):
    supplier = SecondSupplierSerializer()

    class Meta:
        model = ChainLink
        fields = ('id', 'title', 'type', 'supplier',)


class ChainLinkSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    type = serializers.SerializerMethodField()
    contact = ContactsSerializer()
    product = ProductsSerializer(many=True)

    @staticmethod
    def get_type(obj: ChainLink) -> str:
        return obj.get_type_display()

    class Meta:
        model = ChainLink
        fields = '__all__'


class ChainLinkCreateSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=ChainLink.objects.all())

    class Meta:
        model = ChainLink
        fields = ('title', 'type', 'supplier', 'contact', 'product', 'debt')
        read_only_fields = ['dedt']
