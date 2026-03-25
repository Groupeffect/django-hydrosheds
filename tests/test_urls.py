"""Tests for hydrosheds.urls module."""

from django.test import SimpleTestCase
from hydrosheds import urls, views
from rest_framework.reverse import reverse


class TestUrlPatterns(SimpleTestCase):
    """Tests that the router registers all expected URL patterns."""

    def _get_route_names(self):
        return [url.name for url in urls.urlpatterns]

    def _get_route_basenames(self):
        return [prefix for prefix, viewset, basename in urls.router.registry]

    # ------------------------------------------------------------------
    # Router registry
    # ------------------------------------------------------------------

    def test_router_is_default_router(self):
        from rest_framework.routers import DefaultRouter

        self.assertIsInstance(urls.router, DefaultRouter)

    def test_registered_count(self):
        self.assertEqual(len(urls.router.registry), 4)

    def test_hydrolake_registered(self):
        basenames = self._get_route_basenames()
        self.assertIn("HydroLakePoint", basenames)

    def test_hydroriver_registered(self):
        basenames = self._get_route_basenames()
        self.assertIn("HydroRiverLine", basenames)

    def test_hydrowaste_registered(self):
        basenames = self._get_route_basenames()
        self.assertIn("HydroWastePoint", basenames)

    def test_hydrobasin_registered(self):
        basenames = self._get_route_basenames()
        self.assertIn("HydroBasinPolygon", basenames)

    # ------------------------------------------------------------------
    # ViewSet binding
    # ------------------------------------------------------------------

    def _get_viewset_for_prefix(self, prefix):
        for p, vs, bn in urls.router.registry:
            if p == prefix:
                return vs
        return None

    def test_hydrolake_viewset(self):
        self.assertIs(
            self._get_viewset_for_prefix("HydroLakePoint"),
            views.HydroLakePointViewSet,
        )

    def test_hydroriver_viewset(self):
        self.assertIs(
            self._get_viewset_for_prefix("HydroRiverLine"),
            views.HydroRiverLineViewSet,
        )

    def test_hydrowaste_viewset(self):
        self.assertIs(
            self._get_viewset_for_prefix("HydroWastePoint"),
            views.HydroWastePointViewSet,
        )

    def test_hydrobasin_viewset(self):
        self.assertIs(
            self._get_viewset_for_prefix("HydroBasinPolygon"),
            views.HydroBasinViewSet,
        )

    # ------------------------------------------------------------------
    # URL patterns generated
    # ------------------------------------------------------------------

    def test_urlpatterns_not_empty(self):
        self.assertTrue(len(urls.urlpatterns) > 0)

    def test_list_routes_exist(self):
        route_names = self._get_route_names()
        for basename in [
            "HydroLakePoint",
            "HydroRiverLine",
            "HydroWastePoint",
            "HydroBasinPolygon",
        ]:
            self.assertIn(f"{basename}-list", route_names)

    def test_detail_routes_exist(self):
        route_names = self._get_route_names()
        for basename in [
            "HydroLakePoint",
            "HydroRiverLine",
            "HydroWastePoint",
            "HydroBasinPolygon",
        ]:
            self.assertIn(f"{basename}-detail", route_names)

    # ------------------------------------------------------------------
    # Reverse URLs
    # ------------------------------------------------------------------

    def test_reverse_hydrolake_list(self):
        url = reverse("HydroLakePoint-list", urlconf="hydrosheds.urls")
        self.assertEqual(url, "/HydroLakePoint/")

    def test_reverse_hydroriver_list(self):
        url = reverse("HydroRiverLine-list", urlconf="hydrosheds.urls")
        self.assertEqual(url, "/HydroRiverLine/")

    def test_reverse_hydrowaste_list(self):
        url = reverse("HydroWastePoint-list", urlconf="hydrosheds.urls")
        self.assertEqual(url, "/HydroWastePoint/")

    def test_reverse_hydrobasin_list(self):
        url = reverse("HydroBasinPolygon-list", urlconf="hydrosheds.urls")
        self.assertEqual(url, "/HydroBasinPolygon/")

    def test_reverse_hydrolake_detail(self):
        url = reverse("HydroLakePoint-detail", args=[1], urlconf="hydrosheds.urls")
        self.assertEqual(url, "/HydroLakePoint/1/")

    def test_reverse_hydroriver_detail(self):
        url = reverse("HydroRiverLine-detail", args=[1], urlconf="hydrosheds.urls")
        self.assertEqual(url, "/HydroRiverLine/1/")

    def test_reverse_hydrowaste_detail(self):
        url = reverse("HydroWastePoint-detail", args=[1], urlconf="hydrosheds.urls")
        self.assertEqual(url, "/HydroWastePoint/1/")

    def test_reverse_hydrobasin_detail(self):
        url = reverse("HydroBasinPolygon-detail", args=[1], urlconf="hydrosheds.urls")
        self.assertEqual(url, "/HydroBasinPolygon/1/")
