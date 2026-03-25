from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from hydrosheds import serializers


class HydroLakePointViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HydroLakePointSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
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
    search_fields = ["lake_name", "country", "continent"]
    ordering_fields = [
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

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()


class HydroRiverLineViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HydroRiverLineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
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
        "ord_max",
        "ord_min",
        "pfaf_id",
        "pfaf_type",
        "slope_100",
        "pour_long",
        "pour_lat",
    ]
    search_fields = [
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
        "ord_max",
        "ord_min",
        "pfaf_id",
        "pfaf_type",
        "slope_100",
        "pour_long",
        "pour_lat",
    ]
    ordering_fields = [
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
        "ord_max",
        "ord_min",
        "pfaf_id",
        "pfaf_type",
        "slope_100",
        "pour_long",
        "pour_lat",
    ]

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()


class HydroWastePointViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HydroWastePointSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "waste_id",
        "waste_name",
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
    search_fields = ["waste_name", "country", "continent"]
    ordering_fields = [
        "waste_id",
        "waste_name",
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

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()


class HydroBasinViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HydroBasinPolygonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "basin_id",
        "main_riv",
        "length_km",
        "dist_dn_km",
        "dist_up_km",
        "catch_skm",
        "upland_skm",
        "endorheic",
        "dis_av_cms",
        "ord_stra",
        "ord_max",
        "ord_min",
        "pfaf_id",
        "pfaf_type",
        "slope_100",
        "pour_long",
        "pour_lat",
    ]
    search_fields = [
        "basin_id",
        "main_riv",
        "length_km",
        "dist_dn_km",
        "dist_up_km",
        "catch_skm",
        "upland_skm",
        "endorheic",
        "dis_av_cms",
        "ord_stra",
        "ord_max",
        "ord_min",
        "pfaf_id",
        "pfaf_type",
        "slope_100",
        "pour_long",
        "pour_lat",
    ]
    ordering_fields = [
        "basin_id",
        "main_riv",
        "length_km",
        "dist_dn_km",
        "dist_up_km",
        "catch_skm",
        "upland_skm",
        "endorheic",
        "dis_av_cms",
        "ord_stra",
        "ord_max",
        "ord_min",
        "pfaf_id",
        "pfaf_type",
        "slope_100",
        "pour_long",
        "pour_lat",
    ]

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()
