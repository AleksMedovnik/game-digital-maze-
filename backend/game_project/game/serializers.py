from rest_framework import serializers
from .models import Matrices


class MatricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matrices
        fields = ('id', 'matrix')
