from django.contrib.auth.models import User
from rest_framework import serializers


# Создание модели для обработки данных.
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # Отображение данных.
    class Meta:
        model = User
        fields = ['id', 'username', 'password']  # Отображение выборочно.
        # fields = '__all__'  # Отображение всех данных.

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'])
        return user
