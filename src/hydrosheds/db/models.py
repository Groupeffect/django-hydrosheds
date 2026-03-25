from hydrosheds.db import core


class HydroBasin(core.HydroBasinPolygon):
    class Meta:
        app_label = "hydrosheds"


class HydroRiver(core.HydroRiverLine):
    class Meta:
        app_label = "hydrosheds"


class HydroLake(core.HydroLakePoint):
    class Meta:
        app_label = "hydrosheds"


class HydroWaste(core.HydroWastePoint):
    class Meta:
        app_label = "hydrosheds"
