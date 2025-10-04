from rest_framework import serializers
from .models import listings

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = listing
        fields = '__all__'  # includes all fields from the Listing model
