from django.db import models


class Contacts(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=55, null=True, blank=True)
    city = models.CharField(max_length=55, null=True, blank=True)
    street = models.CharField(max_length=55, null=True, blank=True)
    house_number = models.CharField(max_length=55, null=True, blank=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number}'


class Products(models.Model):
    title = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.title}, {self.model}'


class ChainLink(models.Model):
    class Type(models.IntegerChoices):
        factory = 1, 'Завод'
        retail_network = 2, 'Ретальную сеть'
        individual_entrepreneur = 3, 'Индивидуальный предприниматель'

    title = models.CharField(max_length=255)
    type = models.IntegerField(choices=Type.choices)
    contact = models.ForeignKey(Contacts, on_delete=models.PROTECT, null=True, blank=True)
    product = models.ManyToManyField(Products, blank=True)
    supplier = models.ForeignKey('sales_network.ChainLink', null=True, blank=True, on_delete=models.SET_NULL)
    debt = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Звено'
        verbose_name_plural = 'Звенья'

    def __str__(self):
        return f'{self.title}'
