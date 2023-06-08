from rest_framework import serializers
from advance_django.models import Comments,Category
# class PostSerializer(serializers.Serializer):
#     title=serializers.CharField()
#     email=serializers.EmailField()

class PostSerializer(serializers.ModelSerializer):
    snippet=serializers.ReadOnlyField(source='get_snippet')

    class Meta:
        model=Comments
        fields=['title','email','description','snippet']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name']        