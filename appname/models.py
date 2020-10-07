from django.db import models

class Candidate(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)

class Recruiter(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)

class Task(models.Model):
   title = models.CharField(max_length=50, unique=True)

class Grade(models.Model):
   value = models.IntegerField(blank=True, null=True)
   candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='grades') 
   recruiter = models.ForeignKey(Recruiter, null=True, on_delete=models.SET_NULL)
   task = models.ForeignKey(Task, on_delete=models.CASCADE)