from .models import Matrices
from rest_framework.generics import RetrieveAPIView
from .serializers import MatricesSerializer


class MatrixView(RetrieveAPIView):
    queryset = Matrices.objects.all()
    serializer_class = MatricesSerializer