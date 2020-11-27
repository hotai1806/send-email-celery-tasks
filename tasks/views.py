from django.shortcuts import render
from .tasks import run_in_10s
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site


@api_view(["GET", ])
def get_respone(request):
    current_site = get_current_site(request)
    run_in_10s.delay()
    host = request.META["HTTP_HOST"]

    return Response(data={"domain": "domain1", "host": host, "current-site": current_site.domain}, status=HTTP_200_OK)
