# This file will define how how Problem model ggets converted to JSON and back
# Serializers are like translators:
# They convert Django model data (from DB) to JSON (for API responses)
# They handle data validation and control which fields are visible in API

from rest_framework import serializers 
from .models import Problem

class ProblemSerializer(serializers.ModelSerializer):
    # Meta is special inner class used for configuration
    class Meta:
        # passing the Problem class itself
        # It tells DRF that this serializer is for Problem class
        model = Problem
        fields = ['id', 'title', 'difficulty', 'topic', 'notes', 'solved_date'] # fields you want to expose in the API
        
    
