from django.urls import path
from . import views

urlpatterns = [
   path('', views.candidate_list, name='candidate_list'),
   path('api/add-mark', views.add_mark, name='add_mark')
]