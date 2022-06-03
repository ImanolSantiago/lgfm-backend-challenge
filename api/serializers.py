from rest_framework import serializers

class productSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()
    depth = serializers.IntegerField()

class bookSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    

class userSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    username = serializers.CharField()

class basketSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField()
    owner_id = serializers.CharField()