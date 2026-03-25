from rest_framework import serializers
from hydrosheds.db import models


class HydroLakePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HydroLake
        fields = "__all__"


class HydroRiverLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HydroRiver
        fields = "__all__"


class HydroWastePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HydroWaste
        fields = "__all__"


class HydroBasinPolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HydroBasin
        fields = "__all__"
