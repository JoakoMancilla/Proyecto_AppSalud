from rest_framework import serializers
from .models import Paciente
from .models import Cama

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id','genero','edad','motivoDerivacion','prestacionRequerida']