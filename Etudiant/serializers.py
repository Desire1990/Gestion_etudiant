from .models import *
from rest_framework import serializers

class CampusSerializer(serializers.ModelSerializer):
	class Meta:
		model=Campus
		fields='__all__'

class DepartementSerializer(serializers.ModelSerializer):
	class Meta:
		model=Departement
		fields='__all__'

class FaculteSerializer(serializers.ModelSerializer):
	class Meta:
		model=Faculte
		fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Student
		fields='__all__'
class InstitutSerializer(serializers.ModelSerializer):
	class Meta:
		model=Institut
		fields='__all__'