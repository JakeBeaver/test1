from django.db import models

# Create your models here.
class quizModel(models.Model):
	teacher = models.TextField()
	subject = models.TextField()
	answers = models.TextField()
	date = models.DateTimeField(auto_now_add = "true")
	
