import django_tables2 as tables
from .models import ProductModel
class ProductTable(tables.Table):
    class Meta:
        model = ProductModel
