from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from dashboard.models import Challenge, Company
from .models import Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'picture', 'occupation', 'tags', 'city')


class CompanySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
        # fields = ('name', 'tags')


class ChallengeSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    profile = ProfileSerializer(read_only=True)

    interested = serializers.SerializerMethodField()

    class Meta:
        model = Challenge
        fields = '__all__'
        # fields = ( 'company', 'tags', 'profile')


    def get_interested(self,obj):
        return ProfileSerializer(obj.interested(), many=True).data

