from rest_framework import serializers
import models

class quizSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.quizModel
		fields = ('id', 'subject', 'teacher', 'date', 'answers')

