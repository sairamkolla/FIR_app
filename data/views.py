from django.shortcuts import render_to_response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from data.models import fir
import json
from serializers import FirSerializer

# Create your views here.

def Search(request):
    return render_to_response('data/search.html')

def Home(request):
    return render_to_response('data/home.html')

@api_view(['POST'])
def AddFir(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        #check name
        try:
            a = postdata['name']
        except:
            return Response({'error':'Username cannot be empty'})
        if a == '':
            return Response({'error':'Username cannot be empty'})
        try:
            b = postdata['address']
        except:
            return Response({'error':'Address cannot be empty'})
        if b == '':
            return Response({'error':'Address cannot be empty'})
        try:
            c = postdata['description']
        except:
            return Response({'error':'Description cannot be empty'})
        if c == '':
            return Response({'error':'Description cannot be empty'})
        newfir = fir(name = a, address = b, description = c)
        newfir.save()
        return Response({'ok':request.body})

@api_view(['POST'])
def GetFir(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        try:
            temp = postdata['datestring']
        except:
            return Response({'error':'Please Select The dates'})
        if temp == '':
            return Response({'error':'Please Select The dates'})
        fromdate = temp.split('-')[0].strip()
        todate = temp.split('-')[1].strip()
        fromdate = converttodate(fromdate)
        todate = converttodate(todate)
        posts = fir.objects.filter(date__range=[fromdate,todate])
        serailizer = FirSerializer(posts,many=True)
        return Response(serailizer.data)

def converttodate(ref):
    temp = ref.split('/')
    return temp[2] + '-' + temp[0] + '-' + temp[1]