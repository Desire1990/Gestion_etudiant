from rest_framework import viewsets, filters
from .models import *
from .serializers import *


class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name')

class FaculteViewSet(viewsets.ModelViewSet):
    queryset = Faculte.objects.all()
    serializer_class = FaculteSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name')

class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name')

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('student_id', 'fullname')

class InstitutViewSet(viewsets.ModelViewSet):
    queryset = Institut.objects.all()
    serializer_class = InstitutSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name')
