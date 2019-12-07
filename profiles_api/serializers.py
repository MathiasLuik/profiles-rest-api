from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our apiView"""
    name = serializers.CharField(max_length=10)
    #names = serializerss.CharField(max_length=10)
