import factory


from ..models import Product


class ProductFactory(factory.DjangoModelFactory):

    class Meta:
        model = Product

    title = 'Burger'
    description = 'Cheese Burger'
