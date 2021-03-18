import json

from django.http import JsonResponse
from rest_framework.decorators import api_view

from app.helpers.cosmosdb_client import CosmosDb
from app.helpers.yacht import Yacht

cosmos = CosmosDb()


@api_view(["GET"])
def all(request):
    data = cosmos.all()
    return JsonResponse(data, safe=False)


@api_view(["GET"])
def get(request, uuid):
    try:
        data = cosmos.get(uuid.__str__())
        return JsonResponse(data, safe=False)
    except Exception as e:
        raise e


@api_view(["POST"])
def post(request):
    try:
        data = json.loads(request.body)
        yacht = Yacht(**data)
        response = cosmos.create(yacht)
        return JsonResponse(response, safe=False)
    except Exception as e:
        raise e