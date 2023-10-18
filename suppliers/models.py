from django.db import models

NULLABLE = {'blank': True, 'null': True}


class ChainElement(models.Model):
    """Add Model Supplier
    (Добавлена Модель Supplier (Поставщик))"""
    CHAIN_LEVEL = (
        (0, 'Factory'),
        (1, 'Retail'),
        (2, 'Entrepreneur')
    )

    name = models.CharField(max_length=150, verbose_name='Supplier Name')
    email = models.EmailField(unique=True, verbose_name='Supplier Email')
    country = models.CharField(max_length=150, verbose_name='Supplier Country')
    city = models.CharField(max_length=150, verbose_name='Supplier Country')
    street = models.CharField(max_length=150, verbose_name='Supplier Country')
    house_number = models.CharField(max_length=150, verbose_name='Supplier Country')
    debt = models.DecimalField(max_digits=15, default=0, decimal_places=2, verbose_name='Debt')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Supplier')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Supplier Created')
    chain_level = models.IntegerField(choices=CHAIN_LEVEL, verbose_name='Chain Level')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Chain Element'
        verbose_name_plural = 'Chain Elements'
        ordering = ['id']
