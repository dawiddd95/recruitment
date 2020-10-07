from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect

from .serializers import CandidateSerializer
from .forms import GradeForm
from .models import Candidate, Recruiter, Task, Grade

@api_view(['GET'])
def candidate_list(request):
   candidates = Candidate.objects.all()
   serializer = CandidateSerializer(candidates, many=True)

   return JsonResponse({'data': serializer.data}, json_dumps_params={'indent': 2})

@api_view(['GET', 'POST'])
def add_mark(request):
   my_form = GradeForm()

   context = {
      'form': my_form,
   }

   if request.method == 'POST':
      my_form = GradeForm(request.POST)

      if my_form.is_valid():
         grades = Grade.objects.filter(
            candidate__id=request.POST['candidate'], 
            task__id=request.POST['task']
         )

         if grades.exists():
            return render(
               request, 
               'appname/add_mark.html', 
               {
                  'error': 'This task for this particular candidate was already grade!',
                  'success': ''
               }
            )
         else: 
            Grade.objects.create(**my_form.cleaned_data)
            return render(
               request, 
               'appname/add_mark.html', 
               {
                  'error': '',
                  'success': 'Grade was added succesfully!'
               }
            )

      else:
         print(my_form.errors)
   
   return render(request, 'appname/add_mark.html', context)