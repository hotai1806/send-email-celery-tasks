from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@api_view(["GET", ])
def get_respone(request):
    return Response(data="domain2", status=HTTP_200_OK)
