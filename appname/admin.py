from django.contrib import admin
from .models import (Candidate, Recruiter, Task, Grade)

admin.site.register(Candidate)
admin.site.register(Recruiter)
admin.site.register(Task)
admin.site.register(Grade)