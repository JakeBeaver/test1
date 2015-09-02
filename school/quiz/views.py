from rest_framework import viewsets
import serializers
import models

# Create your views here.
class quizView(viewsets.ModelViewSet):
	serializer_class = serializers.quizSerializer
	queryset = models.quizModel.objects.all()
