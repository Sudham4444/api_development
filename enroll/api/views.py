from enroll.models import Student
from enroll.api.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class StudentViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        return StudentSerializer
    
    queryset=Student.objects.all()
    seriazer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="List all students",
        responses={200: StudentSerializer(many=True),
                   201: openapi.Response(
                        description="Student added successfully",
                        schema=StudentSerializer
                    ),
                    400: "Bad request"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

