from django.urls import path
from .views import MatrixView

urlpatterns = [
    path('<pk>', MatrixView.as_view())
]
