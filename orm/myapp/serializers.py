from rest_framework import serializers
from .models import *

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
# class EmployeeSerializers(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField()

#     def validate_name(self,value):
#         if Customer.objects.filter(name = value).exists():
#             raise serializers.ValidationError('object with same name already exist')
#         return value
    
#     def validate(self,data):
#         nm = data.get('name')
#         em = data.get('email')
#         if nm.lower() == 'rahul' and em.lower() == 'rahul@gmail.com':
#             raise serializers.ValidationError('mail should be unique')
#         return data

#     def create(self, validated_data):
#         return Customer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'