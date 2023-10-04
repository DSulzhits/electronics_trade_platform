from django.db import models

NULLABLE = {'blank': True, 'null': True}


class ChainElement(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=150, verbose_name='Country')
    city = models.CharField(max_length=150, verbose_name='City')
    street = models.CharField(max_length=150, verbose_name='Street')
    house_number = models.CharField(max_length=150, verbose_name='House Number')
    product_name = models.CharField(max_length=150, verbose_name='Product Name')
    product_model = models.CharField(max_length=150, verbose_name='Product Model')
    product_date = models.DateField(verbose_name='Product Date')
    supplier = models.ForeignKey('self', default='null', on_delete=models.SET_NULL, verbose_name='Supplier', **NULLABLE)
    debt = models.DecimalField(max_digits=15, default=0, decimal_places=2, verbose_name='Debt')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')

    class Meta:
        verbose_name = 'Chain Element'
        verbose_name_plural = 'Chain Elements'
        ordering = ['supplier', 'name', ]
