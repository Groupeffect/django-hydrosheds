from django.conf import settings

if not hasattr(settings, "HYDROSHEDS_DISABLE_MODELS"):
    from hydrosheds.db.models import *
elif (
    hasattr(settings, "HYDROSHEDS_DISABLE_MODELS")
    and settings.HYDROSHEDS_DISABLE_MODELS is False
):
    from hydrosheds.db.models import *
else:
    print("set: HYDROSHEDS_DISABLE_MODELS = False, if you want to load models.")
