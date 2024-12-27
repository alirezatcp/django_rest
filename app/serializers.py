from rest_framework import serializers

from app.models import Car

class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    minimum_price = serializers.IntegerField()
    maximum_price = serializers.IntegerField()
    country = serializers.CharField(max_length=100)

    def validate_minimum_price(self, value): # validate a single field
        if value < 0:
            raise serializers.ValidationError('minimum_price must be positive.')

        return value


    def validate(self, data): # validate fields with each other
        if data.get('minimum_price', self.instance.minimum_price if self.instance else 0) > data.get('maximum_price', self.instance.maximum_price if self.instance else 0):
            error = 'maximum price should be greater than minimum price.'
            raise serializers.ValidationError(error)

        return data

    
    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        return car


    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name
        )

        instance.minimum_price = validated_data.get(
            'minimum_price', instance.minimum_price
        )


        instance.maximum_price = validated_data.get(
            'maximum_price', instance.maximum_price
        )

        instance.country = validated_data.get(
            'country', instance.country
        )

        instance.save()

        return instance