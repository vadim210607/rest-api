from django.contrib.auth.models import User
from rest_framework import serializers

from catalog.models import Perfum, Bottle


class UserListAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PerfumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfum
        fields = ('id', 'title', 'content', 'brand', 'bottle')
        # fields = '__all__'


class BottleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottle
        fields = ('id', 'type')


# для тренування в розширеному вигляді
# class PerfumSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField(allow_blank=True)
#     brand_id = serializers.IntegerField()
#     bottle_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Perfum.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.brand_id = validated_data.get('brand_id', instance.brand_id)
#         instance.bottle_id = validated_data.get('bottle_id', instance.bottle_id)
#         instance.save()
#         return instance





