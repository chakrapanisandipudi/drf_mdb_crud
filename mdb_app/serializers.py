from rest_framework import serializers
from mdb_app.models import Tutorials

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorials
        fields = ('id', 'title', 'description', 'published')
