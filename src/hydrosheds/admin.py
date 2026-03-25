from django.contrib import admin
from django.conf import settings


def load_admin():
    from hydrosheds import models

    admin.site.register(models.HydroLake)
    admin.site.register(models.HydroRiver)
    admin.site.register(models.HydroWaste)
    admin.site.register(models.HydroBasin)


if (
    not hasattr(settings, "HYDROSHEDS_DISABLE_MODELS")
    or settings.HYDROSHEDS_DISABLE_MODELS is False
) and (
    not hasattr(settings, "HYDROSHEDS_DISABLE_ADMIN")
    or settings.HYDROSHEDS_DISABLE_ADMIN is False
):
    load_admin()
