from django.urls import path, include
from rest_framework import routers
from genes.views import CheckCodonView


router = routers.DefaultRouter()
router.register('check_codon', CheckCodonView, basename='check_codon')

urlpatterns = [
    path('api/', include(router.urls)),
]
