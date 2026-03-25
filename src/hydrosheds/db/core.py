# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


bn = {"blank": True, "null": True}


class MetaHydroModel(models.Model):
    class Meta:
        abstract = True


class HydroLakePoint(MetaHydroModel):
    """
    HydroLAKES: Global lake distribution
    Version: 1.0 (December 2016)
    Reference: Messager, M.L., et al. (2016). Estimating the volume and age of water stored in global lakes.
    """

    hylak_id = models.PositiveIntegerField(
        primary_key=True, help_text="Unique lake identifier."
    )
    lake_name = models.CharField(
        max_length=40, help_text="Name of lake or reservoir.", **bn
    )
    country = models.CharField(
        max_length=35,
        help_text="Country that the lake (or reservoir) is located in.",
        **bn,
    )
    continent = models.CharField(
        max_length=15,
        help_text="Continent that the lake (or reservoir) is located in.",
        **bn,
    )
    poly_src = models.CharField(
        max_length=10, help_text="Source of original lake polygon.", **bn
    )
    lake_type = models.IntegerField(
        help_text="Indicator for lake type: 1=Lake, 2=Reservoir, 3=Lake control.", **bn
    )
    grand_id = models.IntegerField(
        help_text="ID of the corresponding reservoir in the GRanD database.", **bn
    )
    lake_area = models.FloatField(
        help_text="Lake surface area (i.e. polygon area), in square kilometers.", **bn
    )
    shore_len = models.FloatField(
        help_text="Length of shoreline (i.e. polygon outline), in kilometers.", **bn
    )
    shore_dev = models.FloatField(
        help_text="Shoreline development, measured as the ratio between shoreline length and circumference of a circle with the same area.",
        **bn,
    )
    vol_total = models.FloatField(
        help_text="Total lake or reservoir volume, in million cubic meters.", **bn
    )
    vol_res = models.FloatField(
        help_text="Reported reservoir volume, or storage volume of added lake regulation, in million cubic meters.",
        **bn,
    )
    vol_src = models.IntegerField(
        help_text="1: reported total lake volume, 2: reported total reservoir volume, 3: estimated total lake volume.",
        **bn,
    )
    depth_avg = models.FloatField(help_text="Average lake depth, in meters.", **bn)
    dis_avg = models.FloatField(
        help_text="Average long-term discharge flowing through the lake, in cubic meters per second.",
        **bn,
    )
    res_time = models.FloatField(
        help_text="Average residence time of the lake water, in days.", **bn
    )
    elevation = models.IntegerField(
        help_text="Elevation of lake surface, in meters above sea level.", **bn
    )
    slope_100 = models.FloatField(
        help_text="Average slope within a 100 meter buffer around the lake polygon, in degrees.",
        **bn,
    )
    wshd_area = models.FloatField(
        help_text="Area of the watershed associated with the lake, in square kilometers.",
        **bn,
    )
    pour_long = models.FloatField(
        help_text="Longitude of the lake pour point, in decimal degrees.", **bn
    )
    pour_lat = models.FloatField(
        help_text="Latitude of the lake pour point, in decimal degrees.", **bn
    )
    geom = models.PointField(
        srid=4326, help_text="Geometry of the lake pour point", **bn
    )

    class Meta:
        abstract = True


# Auto-generated `LayerMapping` dictionary for HydroRiversPoint model
HydroLake_mapping = {
    "hylak_id": "Hylak_id",
    "lake_name": "Lake_name",
    "country": "Country",
    "continent": "Continent",
    "poly_src": "Poly_src",
    "lake_type": "Lake_type",
    "grand_id": "Grand_id",
    "lake_area": "Lake_area",
    "shore_len": "Shore_len",
    "shore_dev": "Shore_dev",
    "vol_total": "Vol_total",
    "vol_res": "Vol_res",
    "vol_src": "Vol_src",
    "depth_avg": "Depth_avg",
    "dis_avg": "Dis_avg",
    "res_time": "Res_time",
    "elevation": "Elevation",
    "slope_100": "Slope_100",
    "wshd_area": "Wshd_area",
    "pour_long": "Pour_long",
    "pour_lat": "Pour_lat",
    "geom": "POINT",
}


class HydroRiverLine(MetaHydroModel):
    """
    HydroRIVERS: Global river network delineation
    Version: 1.0 (October 2019)
    Reference: Lehner, B., Grill G. (2013). Global river hydrography and network routing.
    """

    hyriv_id = models.PositiveIntegerField(
        primary_key=True, help_text="Unique identifier for each river reach."
    )
    next_down = models.IntegerField(
        help_text="HYRIV_ID of the next downstream line segment.", **bn
    )
    main_riv = models.IntegerField(
        help_text="HYRIV_ID of the most downstream reach of the connected river basin.",
        **bn,
    )
    length_km = models.FloatField(
        help_text="Length of the river reach segment, in kilometers.", **bn
    )
    dist_dn_km = models.FloatField(
        help_text="Distance from the reach outlet to the final downstream location along the river network, in km.",
        **bn,
    )
    dist_up_km = models.FloatField(
        help_text="Distance from the reach outlet to the most upstream location along the river network, in km.",
        **bn,
    )
    catch_skm = models.FloatField(
        help_text="Area of the catchment that contributes directly to the individual reach, in square kilometers.",
        **bn,
    )
    upland_skm = models.FloatField(
        help_text="Total upstream area, in square kilometers, calculated from the headwaters to the pour point.",
        **bn,
    )
    endorheic = models.IntegerField(
        help_text="Indicator for endorheic (inland) basins without surface flow connection to the ocean.",
        **bn,
    )
    dis_av_cms = models.FloatField(
        help_text="Average long-term discharge estimate for river reach, in cubic meters per second.",
        **bn,
    )
    ord_stra = models.IntegerField(
        help_text="Indicator of river order following the Strahler ordering system.",
        **bn,
    )
    ord_clas = models.IntegerField(
        help_text="Indicator of river order following the classical ordering system.",
        **bn,
    )
    ord_flow = models.IntegerField(
        help_text="Indicator of river order using river flow to distinguish logarithmic size classes.",
        **bn,
    )
    hybas_l12 = models.BigIntegerField(
        help_text="HYBAS_ID of the corresponding HydroBASINS sub-basin in which the river reach resides.",
        **bn,
    )
    geom = models.LineStringField(
        srid=4326, help_text="Geometry of the river reach", **bn
    )

    class Meta:
        abstract = True


# Auto-generated `LayerMapping` dictionary for HydroRiverLine model
HydroRiver_mapping = {
    "hyriv_id": "HYRIV_ID",
    "next_down": "NEXT_DOWN",
    "main_riv": "MAIN_RIV",
    "length_km": "LENGTH_KM",
    "dist_dn_km": "DIST_DN_KM",
    "dist_up_km": "DIST_UP_KM",
    "catch_skm": "CATCH_SKM",
    "upland_skm": "UPLAND_SKM",
    "endorheic": "ENDORHEIC",
    "dis_av_cms": "DIS_AV_CMS",
    "ord_stra": "ORD_STRA",
    "ord_clas": "ORD_CLAS",
    "ord_flow": "ORD_FLOW",
    "hybas_l12": "HYBAS_L12",
    "geom": "LINESTRING",
}


class HydroBasinPolygon(MetaHydroModel):
    """
    HydroBASINS: Global watershed boundaries and sub-basin delineations
    Version: 1.c (July 2014)
    Reference: Lehner, B., Grill G. (2013). Global river hydrography and network routing.
    """

    hybas_id = models.PositiveIntegerField(
        primary_key=True, help_text="Unique basin identifier."
    )
    next_down = models.BigIntegerField(
        help_text="Hybas_id of the next downstream polygon.", **bn
    )
    next_sink = models.BigIntegerField(
        help_text="Hybas_id of the next downstream sink.", **bn
    )
    main_bas = models.BigIntegerField(
        help_text="Hybas_id of the most downstream sink, i.e. the outlet of the main river basin.",
        **bn,
    )
    dist_sink = models.FloatField(
        help_text="Distance from polygon outlet to the next downstream sink along the river network, in kilometers.",
        **bn,
    )
    dist_main = models.FloatField(
        help_text="Distance from polygon outlet to the most downstream sink, i.e. the outlet of the main river basin, in km.",
        **bn,
    )
    sub_area = models.FloatField(
        help_text="Area of the individual polygon (i.e. sub-basin), in square kilometers.",
        **bn,
    )
    up_area = models.FloatField(
        help_text="Total upstream area, in square kilometers, calculated from the headwaters to the polygon location.",
        **bn,
    )
    pfaf_id = models.IntegerField(help_text="The Pfafstetter code.", **bn)
    endo = models.IntegerField(
        help_text="Indicator for endorheic (inland) basins without surface flow connection to the ocean.",
        **bn,
    )
    coast = models.IntegerField(help_text="Indicator for lumped coastal basins.", **bn)
    order = models.IntegerField(
        help_text="Indicator of river order (classical ordering system).", **bn
    )
    sort = models.BigIntegerField(
        help_text="Indicator showing the record number (sequence) in which the original polygons are stored in the shapefile.",
        **bn,
    )
    geom = models.MultiPolygonField(
        srid=4326, help_text="Geometry of the sub-basin polygon", **bn
    )

    class Meta:
        abstract = True


# Auto-generated `LayerMapping` dictionary for HydroBasin model
HydroBasin_mapping = {
    "hybas_id": "HYBAS_ID",
    "next_down": "NEXT_DOWN",
    "next_sink": "NEXT_SINK",
    "main_bas": "MAIN_BAS",
    "dist_sink": "DIST_SINK",
    "dist_main": "DIST_MAIN",
    "sub_area": "SUB_AREA",
    "up_area": "UP_AREA",
    "pfaf_id": "PFAF_ID",
    "endo": "ENDO",
    "coast": "COAST",
    "order": "ORDER",
    "sort": "SORT",
    "geom": "POLYGON",
}


class HydroWastePoint(MetaHydroModel):
    """
    HydroWASTE: Global wastewater treatment plant database
    Date: December 2021
    Version: 1.0

    Reference paper: Ehalt Macedo, H., Lehner, B., Nicell, J. A., Grill, G., Li, J., Limtong, A., Shakya, R.: Distribution and characteristics of wastewater treatment plants within the global river network. Earth System Science Data. 2022.
    Correspondence to: Heloisa Ehalt Macedo (heloisa.ehaltmacedo@mail.mcgill.ca) or Bernhard Lehner (bernhard.lehner@mcgill.ca)
    """

    waste_id = models.BigIntegerField(
        primary_key=True, help_text="ID of WWTP in HydroWASTE"
    )
    source = models.IntegerField(
        **bn,
        help_text="National/regional dataset: 1 = Europe; 2 = United States; 3 = Brazil; 4 = Mexico; 5 = China; 6 = Canada; 7 = Australia; 8 = South Africa; 9 = India; 10 = New Zealand; 11 = Peru; 12 = Remaining Countries",
    )
    org_id = models.CharField(
        max_length=255,
        **bn,
        help_text="ID from national/regional dataset (see reference paper for more information)",
    )
    wwtp_name = models.CharField(
        max_length=255,
        **bn,
        help_text="Name of the WWTP from national/regional dataset (empty if not reported)",
    )
    country = models.CharField(
        max_length=255, **bn, help_text="Country in which WWTP is located"
    )
    cntry_iso = models.CharField(max_length=255, **bn, help_text="Country ISO")
    lat_wwtp = models.FloatField(**bn, help_text="Latitude of reported WWTP location")
    lon_wwtp = models.FloatField(**bn, help_text="Longitude of reported WWTP location")
    qual_loc = models.IntegerField(
        **bn,
        help_text="Quality indicator related to reported WWTP location (see SI of reference paper for more information): 1 = high (tests indicated >80% of reported WWTP locations in country/region to be accurate); 2 = medium (tests indicated between 50% and 80% of reported WWTP locations in country/region to be accurate); 3 = low (tests indicated <50% of reported WWTP locations in country/region to be accurate); 4 = Quality of WWTP locations in country/region not analysed",
    )
    lat_out = models.FloatField(
        **bn,
        help_text="Latitude of the estimated outfall location (see reference paper for more information)",
    )
    lon_out = models.FloatField(
        **bn,
        help_text="Longitude of the estimated outfall location (see reference paper for more information)",
    )
    status = models.CharField(
        max_length=255,
        **bn,
        help_text="Status of the WWTP from national/regional dataset: Closed, Construction Completed, Decommissioned, Non-Operational, Operational, Projected, Proposed, Under Construction, Not Reported (assumed operational)",
    )
    pop_served = models.FloatField(**bn, help_text="Population served by the WWTP")
    qual_pop = models.IntegerField(
        **bn,
        help_text="Quality indicator related to the attribute 'population served' (see reference paper for more information): 1 = Reported as ‘population served’ by national/regional dataset; 2 = Reported as ‘population equivalent’ by national/regional dataset; 3 = Estimated (with wastewater discharge available); 4 = Estimated (without wastewater discharge available)",
    )
    waste_dis = models.FloatField(
        **bn, help_text="Treated wastewater discharged by the WWTP in m3 d-1"
    )
    qual_waste = models.IntegerField(
        **bn,
        help_text="Quality indicator related to the attribute 'Treated wastewater discharged' (see reference paper for more information): 1 = Reported as ‘treated’ by national/regional dataset; 2 = Reported as ‘design capacity’ by national/regional dataset; 3 = Reported but type not identified; 4 = Estimated",
    )
    level = models.CharField(
        max_length=255,
        **bn,
        help_text="Level of treatment of the WWTP: Primary, Secondary, Advanced",
    )
    qual_level = models.IntegerField(
        **bn,
        help_text="Quality indicator related to the attribute 'level of treatment' (see reference paper for more information): 1 = Reported by national/regional dataset; 2 = Estimated",
    )
    df = models.FloatField(
        **bn,
        help_text="Estimated dilution factor (empty if estimated outfall location is the ocean or large lake; see reference paper for more information)",
    )
    hyriv_id = models.BigIntegerField(
        **bn,
        help_text="ID of associated river reach in RiverATLAS at estimated outfall location (link to HydroATLAS database; empty if estimated outfall location is the ocean or an endorheic sink)",
    )
    river_dis = models.FloatField(
        **bn,
        help_text="Estimated river discharge at the WWTP outfall location in m3 s-1 (derived from HydroATLAS database; empty if estimated outfall location is the ocean)",
    )
    coast_10km = models.IntegerField(
        **bn,
        help_text="1 = Estimated outfall location within 10 km of the ocean or a large lake (surface area larger than 500 km2); 0 = Estimated outfall location further than 10 km of the ocean or a large lake (surface area larger than 500 km2)",
    )
    coast_50km = models.IntegerField(
        **bn,
        help_text="1 = Estimated outfall location within 50 km of the ocean or a large lake (surface area larger than 500 km2); 0 = Estimated outfall location further than 50 km of the ocean or a large lake (surface area larger than 500 km2)",
    )
    design_cap = models.FloatField(
        **bn,
        help_text="Design capacity of WWTP as reported in national/regional dataset (empty if not reported)",
    )
    qual_cap = models.IntegerField(
        **bn,
        help_text="Quality indicator related to the attribute 'design capacity': 1 = Reported as design capacity in m3 d-1; 2 = Reported as design capacity in 'population equivalent'; 3 = Not reported",
    )
    geom = models.PointField(srid=4326, **bn, help_text="Geometry of the WWTP")

    class Meta:
        abstract = True


# Auto-generated `LayerMapping` dictionary for HydroWASTE model
HydroWASTE_mapping = {
    "waste_id": "WASTE_ID",
    "source": "SOURCE",
    "org_id": "ORG_ID",
    "wwtp_name": "WWTP_NAME",
    "country": "COUNTRY",
    "cntry_iso": "CNTRY_ISO",
    "lat_wwtp": "LAT_WWTP",
    "lon_wwtp": "LON_WWTP",
    "qual_loc": "QUAL_LOC",
    "lat_out": "LAT_OUT",
    "lon_out": "LON_OUT",
    "status": "STATUS",
    "pop_served": "POP_SERVED",
    "qual_pop": "QUAL_POP",
    "waste_dis": "WASTE_DIS",
    "qual_waste": "QUAL_WASTE",
    "level": "LEVEL",
    "qual_level": "QUAL_LEVEL",
    "df": "DF",
    "hyriv_id": "HYRIV_ID",
    "river_dis": "RIVER_DIS",
    "coast_10km": "COAST_10KM",
    "coast_50km": "COAST_50KM",
    "design_cap": "DESIGN_CAP",
    "qual_cap": "QUAL_CAP",
    "geom": "POINT",
}
