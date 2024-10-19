from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        user =  self.context['request'].user
        print(user, user.is_superuser)
        if user.is_superuser:
            instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
            instance.is_staff = validated_data.get('is_staff', instance.is_staff)
            instance.is_active = validated_data.get('is_active', instance.is_active)
            instance.groups.set(validated_data.get('groups', instance.groups.all()))
            instance.user_permissions.set(validated_data.get('user_permissions', instance.user_permissions.all()))
        else: 
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance