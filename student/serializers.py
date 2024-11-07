from rest_framework import serializers
from .models import Student


# Создание модели для входа в систему пользователей student из бд Student.
class LoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()

    # Проверка данных при входе с хэшированным паролей.
    def validate(self, attrs):
        try:
            student = Student.objects.get(name=attrs['name'])
        except Student.DoesNotExist:
            # Такого пользователя не существует.
            raise serializers.ValidationError(
                'This user does not exist.')
        # Проверка пароля с использованием метода check_password.
        if not student.check_password(attrs['password']):
            # Неверный пароль.
            raise serializers.ValidationError(
                'Invalid password.')

        attrs['student'] = student
        return attrs


# Регистрация нового пользователя student и сохранение в бд Student.
class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # Поля для регистрации.
        fields = ['name', 'username', 'password', 'status', 'level']


# Изменение данных пользователя student в бд Student.
class StudentUpdateSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        # Поля для отображения и редактирования.
        fields = ['name', 'image', 'password', 'phone', 'e_mail',
                  'nickname_tg', 'nickname_inst']

    def get_name(self, obj):
        return f"{obj.name}"

    def update(self, instance, validated_data):
        # Удаление пароля из бд, чтоб не хранился в явном виде.
        password = validated_data.pop('password', None)

        # Обновление остальных редактируемых полей.
        instance = super().update(instance, validated_data)

        # Создание, хэширование и сохранение нового пароля.
        if password:
            instance.set_password(password)
            instance.save()

        return instance
