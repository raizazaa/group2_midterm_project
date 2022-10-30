from django.shortcuts import render
from homepage.models import Advertisement
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.core import serializers
from advertisement.serializers import AdvertisementSerializer
from rest_framework import viewsets



# Create your views here.
@login_required(login_url='/account/login/')
def show_advertisement(request):
    advertisement_item = Advertisement.objects.all().values()
    context = {"list_item": advertisement_item, "username": str(request.user).upper()}   
    return render(request, 'advertisements.html',context)

@login_required(login_url="/account/login/")
def show_json(request):
    data = Advertisement.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

class AdvertisementViewset(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
