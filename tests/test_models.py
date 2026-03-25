"""Tests for hydrosheds.db.core, hydrosheds.db.models, and hydrosheds.serializers modules."""

from django.test import SimpleTestCase
from hydrosheds.db import core, models


# ---------------------------------------------------------------------------
# Core abstract model tests
# ---------------------------------------------------------------------------


class TestMetaHydroModel(SimpleTestCase):
    """Tests for the MetaHydroModel base class."""

    def test_is_abstract(self):
        self.assertTrue(core.MetaHydroModel._meta.abstract)


class TestHydroLakePointCore(SimpleTestCase):
    """Tests for the HydroLakePoint abstract model defined in core."""

    model = core.HydroLakePoint

    def test_is_abstract(self):
        self.assertTrue(self.model._meta.abstract)

    def test_inherits_meta_hydro_model(self):
        self.assertTrue(issubclass(self.model, core.MetaHydroModel))

    def test_docstring_present(self):
        self.assertIn("HydroLAKES", self.model.__doc__)

    def test_expected_fields(self):
        field_names = [f.name for f in self.model._meta.get_fields()]
        expected = [
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
            "geom",
        ]
        for name in expected:
            self.assertIn(name, field_names)

    def test_primary_key(self):
        pk = self.model._meta.pk
        self.assertEqual(pk.name, "hylak_id")

    def test_help_text_on_fields(self):
        for field in self.model._meta.get_fields():
            if hasattr(field, "help_text"):
                self.assertTrue(
                    len(field.help_text) > 0,
                    f"Field '{field.name}' has empty help_text",
                )

    def test_geom_srid(self):
        geom = self.model._meta.get_field("geom")
        self.assertEqual(geom.srid, 4326)


class TestHydroRiverLineCore(SimpleTestCase):
    """Tests for the HydroRiverLine abstract model defined in core."""

    model = core.HydroRiverLine

    def test_is_abstract(self):
        self.assertTrue(self.model._meta.abstract)

    def test_inherits_meta_hydro_model(self):
        self.assertTrue(issubclass(self.model, core.MetaHydroModel))

    def test_docstring_present(self):
        self.assertIn("HydroRIVERS", self.model.__doc__)

    def test_expected_fields(self):
        field_names = [f.name for f in self.model._meta.get_fields()]
        expected = [
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
            "ord_clas",
            "ord_flow",
            "hybas_l12",
            "geom",
        ]
        for name in expected:
            self.assertIn(name, field_names)

    def test_primary_key(self):
        pk = self.model._meta.pk
        self.assertEqual(pk.name, "hyriv_id")

    def test_help_text_on_fields(self):
        for field in self.model._meta.get_fields():
            if hasattr(field, "help_text"):
                self.assertTrue(
                    len(field.help_text) > 0,
                    f"Field '{field.name}' has empty help_text",
                )

    def test_geom_srid(self):
        geom = self.model._meta.get_field("geom")
        self.assertEqual(geom.srid, 4326)


class TestHydroBasinPolygonCore(SimpleTestCase):
    """Tests for the HydroBasinPolygon abstract model defined in core."""

    model = core.HydroBasinPolygon

    def test_is_abstract(self):
        self.assertTrue(self.model._meta.abstract)

    def test_inherits_meta_hydro_model(self):
        self.assertTrue(issubclass(self.model, core.MetaHydroModel))

    def test_docstring_present(self):
        self.assertIn("HydroBASINS", self.model.__doc__)

    def test_expected_fields(self):
        field_names = [f.name for f in self.model._meta.get_fields()]
        expected = [
            "hybas_id",
            "next_down",
            "next_sink",
            "main_bas",
            "dist_sink",
            "dist_main",
            "sub_area",
            "up_area",
            "pfaf_id",
            "endo",
            "coast",
            "order",
            "sort",
            "geom",
        ]
        for name in expected:
            self.assertIn(name, field_names)

    def test_primary_key(self):
        pk = self.model._meta.pk
        self.assertEqual(pk.name, "hybas_id")

    def test_help_text_on_fields(self):
        for field in self.model._meta.get_fields():
            if hasattr(field, "help_text"):
                self.assertTrue(
                    len(field.help_text) > 0,
                    f"Field '{field.name}' has empty help_text",
                )

    def test_geom_srid(self):
        geom = self.model._meta.get_field("geom")
        self.assertEqual(geom.srid, 4326)


class TestHydroWastePointCore(SimpleTestCase):
    """Tests for the HydroWastePoint abstract model defined in core."""

    model = core.HydroWastePoint

    def test_is_abstract(self):
        self.assertTrue(self.model._meta.abstract)

    def test_inherits_meta_hydro_model(self):
        self.assertTrue(issubclass(self.model, core.MetaHydroModel))

    def test_docstring_present(self):
        self.assertIn("HydroWASTE", self.model.__doc__)

    def test_expected_fields(self):
        field_names = [f.name for f in self.model._meta.get_fields()]
        expected = [
            "waste_id",
            "source",
            "org_id",
            "wwtp_name",
            "country",
            "cntry_iso",
            "lat_wwtp",
            "lon_wwtp",
            "qual_loc",
            "lat_out",
            "lon_out",
            "status",
            "pop_served",
            "qual_pop",
            "waste_dis",
            "qual_waste",
            "level",
            "qual_level",
            "df",
            "hyriv_id",
            "river_dis",
            "coast_10km",
            "coast_50km",
            "design_cap",
            "qual_cap",
            "geom",
        ]
        for name in expected:
            self.assertIn(name, field_names)

    def test_primary_key(self):
        pk = self.model._meta.pk
        self.assertEqual(pk.name, "waste_id")

    def test_help_text_on_fields(self):
        for field in self.model._meta.get_fields():
            if hasattr(field, "help_text"):
                self.assertTrue(
                    len(field.help_text) > 0,
                    f"Field '{field.name}' has empty help_text",
                )

    def test_geom_srid(self):
        geom = self.model._meta.get_field("geom")
        self.assertEqual(geom.srid, 4326)


# ---------------------------------------------------------------------------
# LayerMapping dictionary tests
# ---------------------------------------------------------------------------


class TestLayerMappings(SimpleTestCase):
    """Tests that LayerMapping dicts match their corresponding model fields."""

    def _assert_mapping_keys_match_model(self, mapping, model_class):
        model_field_names = {f.name for f in model_class._meta.get_fields()}
        for key in mapping:
            self.assertIn(
                key,
                model_field_names,
                f"Mapping key '{key}' not found in {model_class.__name__} fields",
            )

    def test_hydrolake_mapping(self):
        self._assert_mapping_keys_match_model(
            core.HydroLake_mapping, core.HydroLakePoint
        )

    def test_hydroriver_mapping(self):
        self._assert_mapping_keys_match_model(
            core.HydroRiver_mapping, core.HydroRiverLine
        )

    def test_hydrobasin_mapping(self):
        self._assert_mapping_keys_match_model(
            core.HydroBasin_mapping, core.HydroBasinPolygon
        )

    def test_hydrowaste_mapping(self):
        self._assert_mapping_keys_match_model(
            core.HydroWASTE_mapping, core.HydroWastePoint
        )


# ---------------------------------------------------------------------------
# Concrete model tests (hydrosheds.db.models)
# ---------------------------------------------------------------------------


class TestHydroLakeModel(SimpleTestCase):
    """Tests for the concrete HydroLake model."""

    model = models.HydroLake

    def test_is_not_abstract(self):
        self.assertFalse(self.model._meta.abstract)

    def test_inherits_hydrolake_point(self):
        self.assertTrue(issubclass(self.model, core.HydroLakePoint))

    def test_db_table(self):
        self.assertEqual(self.model._meta.db_table, "hydrosheds_hydrolake")


class TestHydroRiverModel(SimpleTestCase):
    """Tests for the concrete HydroRiver model."""

    model = models.HydroRiver

    def test_is_not_abstract(self):
        self.assertFalse(self.model._meta.abstract)

    def test_inherits_hydroriver_line(self):
        self.assertTrue(issubclass(self.model, core.HydroRiverLine))

    def test_db_table(self):
        self.assertEqual(self.model._meta.db_table, "hydrosheds_hydroriver")


class TestHydroBasinModel(SimpleTestCase):
    """Tests for the concrete HydroBasin model."""

    model = models.HydroBasin

    def test_is_not_abstract(self):
        self.assertFalse(self.model._meta.abstract)

    def test_inherits_hydrobasin_polygon(self):
        self.assertTrue(issubclass(self.model, core.HydroBasinPolygon))

    def test_db_table(self):
        self.assertEqual(self.model._meta.db_table, "hydrosheds_hydrobasin")


class TestHydroWasteModel(SimpleTestCase):
    """Tests for the concrete HydroWaste model."""

    model = models.HydroWaste

    def test_is_not_abstract(self):
        self.assertFalse(self.model._meta.abstract)

    def test_inherits_hydrowaste_point(self):
        self.assertTrue(issubclass(self.model, core.HydroWastePoint))

    def test_db_table(self):
        self.assertEqual(self.model._meta.db_table, "hydrosheds_hydrowaste")
