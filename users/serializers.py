from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile, UserPredictModel1, ResumeUpload


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'avatar', 'bio']

    def get_avatar(self, obj):
        try:
            return obj.profile.avatar.url
        except Exception:
            return '/media/default.jpg'

    def get_bio(self, obj):
        try:
            return obj.profile.bio
        except Exception:
            return ''


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Passwords do not match.'})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            password=validated_data['password1'],
        )
        return user


class ProfileUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(required=False)
    bio = serializers.CharField(required=False, allow_blank=True)
    avatar = serializers.ImageField(required=False)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile = instance.profile
        if 'bio' in validated_data:
            profile.bio = validated_data['bio']
        if 'avatar' in validated_data:
            profile.avatar = validated_data['avatar']
        profile.save()
        return instance


class PredictionInputSerializer(serializers.Serializer):
    Age = serializers.FloatField()
    Gender = serializers.CharField()
    Qualification = serializers.CharField()
    year = serializers.FloatField()
    cgpa = serializers.FloatField()
    Job_Role = serializers.CharField()
    Post_Graduation = serializers.CharField()
    ten_Percentage = serializers.FloatField()
    twelth_Percentage = serializers.FloatField()
    Salary = serializers.FloatField()
    Soft_Skills = serializers.CharField()
    Internship = serializers.CharField()
    Experience = serializers.FloatField()
    Round = serializers.IntegerField()
    Company_Name = serializers.CharField()


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPredictModel1
        fields = '__all__'
        read_only_fields = ['user', 'label', 'created_at']


class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeUpload
        fields = ['id', 'name', 'email', 'job_role', 'file', 'uploaded_at',
                  'processed', 'ats_score', 'gemini_response', 'suggestions',
                  'course_products', 'alternative_roles', 'role_courses']
        read_only_fields = ['user', 'uploaded_at', 'processed', 'ats_score',
                           'gemini_response', 'suggestions', 'course_products',
                           'alternative_roles', 'role_courses']
