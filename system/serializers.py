from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class UserLoginSerializer(serializers.Serializer):
    """
    Сериализатор для входа пользователя
    """
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserLogoutSerializer(serializers.Serializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователя
    """
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, data):
        """
        Проверка совпадения паролей.
        """
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Пароли не совпадают.")

        return data

    def create(self, validated_data):
        """
        Создание пользователя при регистрации.
        """
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        return user
