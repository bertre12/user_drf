from rest_framework import serializers
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    # Сумма всех баллов за задания.
    total_points = serializers.SerializerMethodField()

    class Meta:
        model = Student
        # Поля для отображения.
        fields = ['id', 'name', 'number_of_points', 'total_points']

    def get_total_points(self, obj):
        # Суммируем баллы за задания, связанные со студентом.
        return sum(task.points_task for task in obj.tasks.all())
