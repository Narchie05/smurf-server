from django.db import models

class Smurf(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ('name',)