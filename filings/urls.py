from django.urls import path, re_path
import re
from . import views

urlpatterns = [
    path('analyzestatements', views.updateStatements, name="analyze"),
    path('fetchfilings', views.getDatabaseFilings, name="fetchfilings")
]
