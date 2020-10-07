from django import forms

from .models import Grade, Recruiter, Task, Candidate

class GradeForm(forms.ModelForm):
   class Meta:
      model = Grade

      candidate = forms.ModelChoiceField(Candidate.objects.all())
      recruiter = forms.ModelChoiceField(Recruiter.objects.all())
      task = forms.ModelChoiceField(Task.objects.all())

      fields = [
         'value',
         'candidate',
         'recruiter',
         'task'
      ]