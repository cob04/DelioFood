from django.test import TestCase

from .model_factory import LocationFactory


class LocationMethodTests(TestCase):

    def setUp(self):
        self._location = LocationFactory()

    def test_location_string_representation(self):
        self.assertEqual(str(self._location), "Westlands")
