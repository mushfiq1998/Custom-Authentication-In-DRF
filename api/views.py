from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from api.customauth import CustomAuthentication

# Create your views here.
'''ModelViewSet class creates CRUD API behind the scene without defining 
create(), get(), update() and delete() methods,'''
class StudentModelViewSet(viewsets.ModelViewSet):
    # queryset = model_name.objects.all(), Here queryset is keyword
    queryset = Student.objects.all()
    # Here, serializer_class is a keyword
    serializer_class = StudentSerializer
    # Add custom authentication  and permission to this API
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
