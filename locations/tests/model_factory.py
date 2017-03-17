import factory

from ..models import (Location)


class LocationFactory(factory.DjangoModelFactory):

    class Meta:
        model = Location

    name = "Westlands"
    overview = "West side of nairobi?"
