import factory

from shop.tests.model_factory import ProductFactory, VariationFactory

from ..models import Order, OrderItem


class OrderFactory(factory.DjangoModelFactory):

    class Meta:
        model = Order

    first_name='James'
    last_name='Bond'
    email='bond@00.com'
    phone='0700000000'
    address='Accross the river'
    directions='1st Floor Room 00'


class OrderItemFactory(factory.DjangoModelFactory):

    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    variation = factory.SubFactory(VariationFactory)
    unit_price = 250
    quantity = 1
    instructions = "Moderate salt"
