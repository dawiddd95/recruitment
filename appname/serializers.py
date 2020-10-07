from django.db.models import Avg
from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):

   pk = serializers.SerializerMethodField('get_pk_from_candidate')
   full_name = serializers.SerializerMethodField('get_full_name_from_candidate')
   avg_grade = serializers.SerializerMethodField('get_avg_grade')
   grades = serializers.SlugRelatedField(many=True, read_only=True, slug_field='value')
   
   class Meta: 
      model = Candidate
      fields = ['pk', 'full_name', 'avg_grade', 'grades']

   def get_pk_from_candidate(self, candidate):
      return candidate.id

   
   def get_full_name_from_candidate(self, candidate):
      data = (candidate.first_name, candidate.last_name)
      full_name = ' '.join(data)

      return full_name

   def get_avg_grade(self, candidate):
      return candidate.grades.aggregate(Avg('value'))['value__avg']