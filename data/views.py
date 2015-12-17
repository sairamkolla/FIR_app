from django.shortcuts import render_to_response
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
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
        try:
            b = postdata['address']
        except:
            return Response({'error':'Address cannot be empty'})
        try:
            c = postdata['description']
        except:
            return Response({'error':'Description cannot be empty'})

        #if postdata['name'] == '':
        #    return Response({'error':'Username cannot be empty'})
        #elif postdata['address'] == '':
        #    return Response({'error':'Address cannot be empty'})
        #elif postdata['description'] == '':
        #    return Response({'error':'Description cannot be empty'})
        #else:
        return Response({'ok':request.body})
