from hydrosheds.db import core


class HydroBasin(core.HydroBasinPolygon):
    pass


class HydroRiver(core.HydroRiverLine):
    pass


class HydroLake(core.HydroLakePoint):
    pass


class HydroWaste(core.HydroWastePoint):
    pass
