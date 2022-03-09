from rest_framework import routers

from Etudiant.viewsets import *

router = routers.DefaultRouter()

router.register('faculte', CampusViewSet)
router.register('campus', FaculteViewSet)
router.register('departement', DepartementViewSet)
router.register('student', StudentViewSet)
router.register('institut', InstitutViewSet)