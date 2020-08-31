from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    first_name = serializers.SerializerMethodField(read_only=True)
    last_name = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)
    number = serializers.SerializerMethodField(read_only=True)
    address1 = serializers.SerializerMethodField(read_only=True)
    address2 = serializers.SerializerMethodField(read_only=True)
    city = serializers.SerializerMethodField(read_only=True)
    postal = serializers.SerializerMethodField(read_only=True)
    
    
    class Meta:
        model = Profile
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'number',
            'address1',
            'address2',
            'city',
            'postal',

        ]
    def get_username(self, obj):
        return obj.user.username

    def get_first_name(self, obj):
        return obj.user.first_name
    
    def get_last_name(self, obj):
        return obj.user.last_name

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    def get_number(self, obj):
        return obj.user.number

    def get_address1(self, obj):
        return obj.address1
    
    def get_address2(self, obj):
        return obj.address2

    def get_city(self, obj):
        return obj.city

    def get_postal(self, obj):
        return obj.postal


class ProfileUpdateSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Profile
        fields = [
            
            'address1',
            'address2',
            'city',
            'postal',
        ]

    def get_username(self, obj):
        return obj.user.username

    def get_first_name(self, obj):
        return obj.user.first_name
    
    def get_last_name(self, obj):
        return obj.user.last_name

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    def get_number(self, obj):
        return obj.user.number

    def get_address1(self, obj):
        return obj.address1
    
    def get_address2(self, obj):
        return obj.address2

    def get_city(self, obj):
        return obj.city

    def get_postal(self, obj):
        return obj.postal