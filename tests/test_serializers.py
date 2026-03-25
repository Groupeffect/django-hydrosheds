"""Tests for hydrosheds.db.core, hydrosheds.db.models, and hydrosheds.serializers modules."""

from django.test import SimpleTestCase
from hydrosheds.db import models


# ---------------------------------------------------------------------------
# Serializer tests
# ---------------------------------------------------------------------------

from rest_framework.serializers import ModelSerializer
from hydrosheds import serializers


class TestHydroLakePointSerializer(SimpleTestCase):
    """Tests for HydroLakePointSerializer."""

    serializer_class = serializers.HydroLakePointSerializer

    def test_is_model_serializer(self):
        self.assertTrue(issubclass(self.serializer_class, ModelSerializer))

    def test_model(self):
        self.assertIs(self.serializer_class.Meta.model, models.HydroLake)

    def test_fields_all(self):
        self.assertEqual(self.serializer_class.Meta.fields, "__all__")

    def test_serializer_fields_match_model(self):
        serializer = self.serializer_class()
        model_field_names = {f.name for f in models.HydroLake._meta.get_fields()}
        for field_name in serializer.fields:
            self.assertIn(field_name, model_field_names)


class TestHydroRiverLineSerializer(SimpleTestCase):
    """Tests for HydroRiverLineSerializer."""

    serializer_class = serializers.HydroRiverLineSerializer

    def test_is_model_serializer(self):
        self.assertTrue(issubclass(self.serializer_class, ModelSerializer))

    def test_model(self):
        self.assertIs(self.serializer_class.Meta.model, models.HydroRiver)

    def test_fields_all(self):
        self.assertEqual(self.serializer_class.Meta.fields, "__all__")

    def test_serializer_fields_match_model(self):
        serializer = self.serializer_class()
        model_field_names = {f.name for f in models.HydroRiver._meta.get_fields()}
        for field_name in serializer.fields:
            self.assertIn(field_name, model_field_names)


class TestHydroWastePointSerializer(SimpleTestCase):
    """Tests for HydroWastePointSerializer."""

    serializer_class = serializers.HydroWastePointSerializer

    def test_is_model_serializer(self):
        self.assertTrue(issubclass(self.serializer_class, ModelSerializer))

    def test_model(self):
        self.assertIs(self.serializer_class.Meta.model, models.HydroWaste)

    def test_fields_all(self):
        self.assertEqual(self.serializer_class.Meta.fields, "__all__")

    def test_serializer_fields_match_model(self):
        serializer = self.serializer_class()
        model_field_names = {f.name for f in models.HydroWaste._meta.get_fields()}
        for field_name in serializer.fields:
            self.assertIn(field_name, model_field_names)


class TestHydroBasinPolygonSerializer(SimpleTestCase):
    """Tests for HydroBasinPolygonSerializer."""

    serializer_class = serializers.HydroBasinPolygonSerializer

    def test_is_model_serializer(self):
        self.assertTrue(issubclass(self.serializer_class, ModelSerializer))

    def test_model(self):
        self.assertIs(self.serializer_class.Meta.model, models.HydroBasin)

    def test_fields_all(self):
        self.assertEqual(self.serializer_class.Meta.fields, "__all__")

    def test_serializer_fields_match_model(self):
        serializer = self.serializer_class()
        model_field_names = {f.name for f in models.HydroBasin._meta.get_fields()}
        for field_name in serializer.fields:
            self.assertIn(field_name, model_field_names)
