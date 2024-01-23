from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from django.http import HttpResponseServerError
from .helper import fetchDistrictData, fetchLanguageData, DataNotFoundError
from .services import populate_database_from_csv

def index(request): 
    populate_database_from_csv()
    template = loader.get_template("index.html")
    return HttpResponse(template.render(request=request))

def plotPerDistrict(request):
    template = loader.get_template("plot_schoolPDistrict.html")
    return HttpResponse(template.render(request=request))

@require_GET
def dataPerDistrict(request):
    try:
        response_data = fetchDistrictData()
        response = JsonResponse({"data": response_data})
    except DataNotFoundError as e:
        response = HttpResponseServerError(str(e))

    return response

def plotPerLanguage(request):
    template = loader.get_template("plot_plotPerLanguage.html")
    return HttpResponse(template.render(request=request))

@require_GET
def dataPerLanguage(request):
    try:
        response_data = fetchLanguageData()
        response = JsonResponse({"data": response_data})
    except DataNotFoundError as e:
        response = HttpResponseServerError(str(e))

    return response
