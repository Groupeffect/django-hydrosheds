"""Tests for hydrosheds.views module."""

from django.test import SimpleTestCase
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend

from hydrosheds import views, serializers
from hydrosheds.db import models


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

EXPECTED_FILTER_BACKENDS = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
EXPECTED_PERMISSIONS = [permissions.IsAuthenticatedOrReadOnly]


class _ViewSetTestMixin:
    """Common assertions shared across all viewset test classes."""

    viewset_class = None
    expected_serializer = None
    expected_model = None
    expected_filterset_fields = []
    expected_search_fields = []
    expected_ordering_fields = []

    def test_is_model_viewset(self):
        self.assertTrue(issubclass(self.viewset_class, viewsets.ModelViewSet))

    def test_serializer_class(self):
        self.assertIs(self.viewset_class.serializer_class, self.expected_serializer)

    def test_permission_classes(self):
        self.assertEqual(self.viewset_class.permission_classes, EXPECTED_PERMISSIONS)

    def test_filter_backends(self):
        self.assertEqual(self.viewset_class.filter_backends, EXPECTED_FILTER_BACKENDS)

    def test_filterset_fields(self):
        self.assertEqual(
            list(self.viewset_class.filterset_fields),
            self.expected_filterset_fields,
        )

    def test_search_fields(self):
        self.assertEqual(
            list(self.viewset_class.search_fields),
            self.expected_search_fields,
        )

    def test_ordering_fields(self):
        self.assertEqual(
            list(self.viewset_class.ordering_fields),
            self.expected_ordering_fields,
        )

    def test_has_get_queryset(self):
        self.assertTrue(hasattr(self.viewset_class, "get_queryset"))


# ---------------------------------------------------------------------------
# HydroLakePointViewSet
# ---------------------------------------------------------------------------


class TestHydroLakePointViewSet(_ViewSetTestMixin, SimpleTestCase):
    """Tests for HydroLakePointViewSet."""

    viewset_class = views.HydroLakePointViewSet
    expected_serializer = serializers.HydroLakePointSerializer
    expected_model = models.HydroLake
    expected_filterset_fields = [
        "hylak_id",
        "lake_name",
        "country",
        "continent",
        "poly_src",
        "lake_type",
        "grand_id",
        "lake_area",
        "shore_len",
        "shore_dev",
        "vol_total",
        "vol_res",
        "vol_src",
        "depth_avg",
        "dis_avg",
        "res_time",
        "elevation",
        "slope_100",
        "wshd_area",
        "pour_long",
        "pour_lat",
    ]
    expected_search_fields = ["lake_name", "country", "continent"]
    expected_ordering_fields = [
        "hylak_id",
        "lake_name",
        "country",
        "continent",
        "poly_src",
        "lake_type",
        "grand_id",
        "lake_area",
        "shore_len",
        "shore_dev",
        "vol_total",
        "vol_res",
        "vol_src",
        "depth_avg",
        "dis_avg",
        "res_time",
        "elevation",
        "slope_100",
        "wshd_area",
        "pour_long",
        "pour_lat",
    ]


# ---------------------------------------------------------------------------
# HydroRiverLineViewSet
# ---------------------------------------------------------------------------


class TestHydroRiverLineViewSet(_ViewSetTestMixin, SimpleTestCase):
    """Tests for HydroRiverLineViewSet."""

    viewset_class = views.HydroRiverLineViewSet
    expected_serializer = serializers.HydroRiverLineSerializer
    expected_model = models.HydroRiver
    expected_filterset_fields = [
        "hyriv_id",
        "next_down",
        "main_riv",
        "length_km",
        "dist_dn_km",
        "dist_up_km",
        "catch_skm",
        "upland_skm",
        "endorheic",
        "dis_av_cms",
        "ord_stra",
    ]
    expected_search_fields = [
        "hyriv_id",
        "next_down",
        "main_riv",
        "length_km",
        "dist_dn_km",
        "dist_up_km",
        "catch_skm",
        "upland_skm",
        "endorheic",
        "dis_av_cms",
        "ord_stra",
    ]
    expected_ordering_fields = [
        "hyriv_id",
        "next_down",
        "main_riv",
        "length_km",
        "dist_dn_km",
        "dist_up_km",
        "catch_skm",
        "upland_skm",
        "endorheic",
        "dis_av_cms",
        "ord_stra",
    ]


# ---------------------------------------------------------------------------
# HydroWastePointViewSet
# ---------------------------------------------------------------------------


class TestHydroWastePointViewSet(_ViewSetTestMixin, SimpleTestCase):
    """Tests for HydroWastePointViewSet."""

    viewset_class = views.HydroWastePointViewSet
    expected_serializer = serializers.HydroWastePointSerializer
    expected_model = models.HydroWaste
    expected_filterset_fields = [
        "waste_id",
        "country",
    ]
    expected_search_fields = ["country"]
    expected_ordering_fields = [
        "waste_id",
        "country",
    ]


# ---------------------------------------------------------------------------
# HydroBasinViewSet
# ---------------------------------------------------------------------------


class TestHydroBasinViewSet(_ViewSetTestMixin, SimpleTestCase):
    """Tests for HydroBasinViewSet."""

    viewset_class = views.HydroBasinViewSet
    expected_serializer = serializers.HydroBasinPolygonSerializer
    expected_model = models.HydroBasin
    expected_filterset_fields = ["hybas_id"]
    expected_search_fields = ["hybas_id"]
    expected_ordering_fields = ["hybas_id"]
