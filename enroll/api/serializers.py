from enroll.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','email','password']
        extra_kwargs = {
            'name': {'help_text': 'Name of the student'},
            'email': {'help_text': 'Mail id of the student'},
        }

    def validate_title(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError("Title must contain 'django'.")
        return value