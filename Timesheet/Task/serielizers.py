from rest_framework import serializers
from .models import *



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    employee_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'employees', 'employee_ids']
        depth = 1

    def create(self, validated_data):
        employee_ids = validated_data.pop('employee_ids', [])
        task = Task.objects.create(**validated_data)

        employees = Employee.objects.filter(id__in=employee_ids)
        task.employees.set(employees)

        return task

    def update(self, instance, validated_data):
        if 'employee_ids' in validated_data:
            employee_ids = validated_data.pop('employee_ids', [])
            employees = Employee.objects.filter(id__in=employee_ids)
            instance.employees.set(employees)

        return super().update(instance, validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'tasks']
