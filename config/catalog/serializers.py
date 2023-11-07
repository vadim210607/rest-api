from rest_framework import serializers

from catalog.models import Perfum


class PerfumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfum
        fields = ('title', 'brand_id', 'bottle_id')
        # fields = '__all__'

