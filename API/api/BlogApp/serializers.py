
from dataclasses import fields
from rest_framework import serializers
from .models import Articles

# class ArticlesSerializer (serializers.Serializer):
#     titel=serializers.CharField(max_length=100)
#     auther=serializers.CharField(max_length=100)
#     email=serializers.EmailField(max_length=100)
#     date=serializers.DateField()
    
#     def create(self, validated_data):
        
#         return Articles.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.title= validated_data.get('title', instance.title)
#         instance.auther= validated_data.get('auther', instance.auther)
#         instance.email= validated_data.get('email', instance.email)
#         instance.date= validated_data.get('date', instance.date)
        
#         instance.save()
#         return instance

class ArticlesSerializer (serializers.ModelSerializer):
    class Meta:
        model=Articles
        # fields=['id','titel','auther']
        fields='__all__'