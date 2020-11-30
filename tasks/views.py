from django.shortcuts import render
from .tasks import run_in_10s, send_email
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from celery.result import AsyncResult


@api_view(["GET", ])
def get_respone(request):
    current_site = get_current_site(request)
    run_in_10s.delay()
    host = request.META["HTTP_HOST"]

    return Response(data={"domain": "domain1", "host": host, "current-site": current_site.domain}, status=HTTP_200_OK)


@api_view(["GET"])
def get_object(request, pk):
    current_site = get_current_site(request)
    print(current_site, 9999999999999)
    if current_site.domain == 'domain1:8000':
        print("taiiiiiiiiiiiiiiiiisssssssssssssssssssssssssssssssssssiiiiii")

        return Response(data="domain1", status=HTTP_200_OK)
    else:
        return Response(data="pl", status=HTTP_200_OK)

    pass


@api_view(['POST'])
def send_email_with_celery(request):
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    receiver = request.POST.get('receiver')
    data = send_email.delay(subject, message,
                            receiver)
    return Response(data='ok', status=HTTP_200_OK)
    pass
