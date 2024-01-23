import os
import csv
from django.conf import settings
from .models import School
from django.db.models import Count

class DataNotFoundError(Exception):
    pass

def fetchDistrictData():
    if not School.objects.exists():
        raise DataNotFoundError("No data found in the Schools model")

    
    districtsData = list(School.objects.values("district_name").annotate(count=Count("id")).order_by("district_name"))
    result = {
        "districts" : [ item["district_name"] for item in districtsData ],
        "countOfSchools": [ item['count'] for item in districtsData]
    }
    return result

def fetchLanguageData():
    if not School.objects.exists():
        raise DataNotFoundError("No data found in the Schools model")
    
    districtLanguageCount = School.objects.values('district_name', 'moi').annotate(count=Count('moi'))
    districts =  [ item["district_name"] for item in School.objects.values("district_name").distinct().order_by("district_name")]
    languages = [ item['moi'] for item in School.objects.values("moi").distinct().order_by("moi")]
    languageCount: dict = {}
    
    for language in languages:
        languageCount[language] = [0]*len(districts)
        
    for item in districtLanguageCount:
        languageCount[item['moi']][districts.index(item['district_name'])] = item["count"]

    result : dict = {
        "districts" : districts,
        "languages" : languages,
        "languageCount": languageCount
    }
    return result
