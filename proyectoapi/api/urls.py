from django.urls import path,include
from .views import Apicrud

urlpatterns = [

    path('', Apicrud.as_view()),
    path('<int:estudiante_id>/', Apicrud.as_view()),


]
