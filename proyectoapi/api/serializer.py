from rest_framework import serializers
from .models import Estudiante

class EstSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields=["nombre","direccion","carnet"]