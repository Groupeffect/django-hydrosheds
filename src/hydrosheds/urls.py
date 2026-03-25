from rest_framework import routers
from hydrosheds import views

router = routers.DefaultRouter()

router.register(
    r"HydroLakePoint", views.HydroLakePointViewSet, basename="HydroLakePoint"
)
router.register(
    r"HydroRiverLine", views.HydroRiverLineViewSet, basename="HydroRiverLine"
)
router.register(
    r"HydroWastePoint", views.HydroWastePointViewSet, basename="HydroWastePoint"
)
router.register(
    r"HydroBasinPolygon", views.HydroBasinViewSet, basename="HydroBasinPolygon"
)
urlpatterns = router.urls
