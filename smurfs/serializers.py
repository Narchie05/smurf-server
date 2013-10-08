from rest_framework import serializers

from smurfs.models import Smurf

class SmurfSerializer(serializers.ModelSerializer):
	class Meta:
		model = SmurfSerializer
		fields = ('id', 'name', 'created')