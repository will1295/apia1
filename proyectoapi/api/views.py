from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions,status
from .serializer import EstSerializer
from rest_framework.response import Response
from .models import Estudiante
from django.shortcuts import get_object_or_404

class Apicrud(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get_object(self, estudiante_id, user_id):
            return get_object_or_404(Estudiante, id=estudiante_id)


    def post(self,request,*args,**kwargs):
        datos = {
            "nombre":request.data.get("nombre"),
            "direccion":request.data.get("direccion"),
            "carnet":request.data.get("carnet"),
        }
        serializer = EstSerializer(data=datos)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,*args,**kwargs):
        estudiantes = Estudiante.objects.all()
        serializer = EstSerializer(estudiantes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self, request, estudiante_id, *args, **kwargs):
        estudiante_instance = self.get_object(estudiante_id, request.user.id)
        data = {
            'nombre': request.data.get('nombre'),
            'direccion': request.data.get('direccion'),
            'carnet': request.data.get('carnet'),
        }
        serializer = EstSerializer(instance=estudiante_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
    def delete(self, request, estudiante_id, *args, **kwargs):
        estudiante_instance = self.get_object(estudiante_id, request.user.id)
        estudiante_instance.delete()
        return Response("Estudiante eliminado exitosamente", status=status.HTTP_204_NO_CONTENT)

