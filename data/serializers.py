from rest_framework import serializers
from models import fir

class FirSerializer(serializers.ModelSerializer):
    Date = serializers.SerializerMethodField('date')
    Time = serializers.SerializerMethodField('time')
    def time(self,object):
         return object.timestamp.strftime("%I:%M %p ")
    def date(self,object):
         return object.timestamp.strftime("%B %d, %Y")

    class Meta:
        model = fir
        fields = ('name','address','description','Date', 'Time')