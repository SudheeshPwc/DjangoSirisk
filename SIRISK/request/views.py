from django.shortcuts import render
from request.models import TransRequest,TransResponse
from rest_framework import generics
from request.serailizers import TransRequestSerailizer, TransResponseSerailizer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.db import connection
from django.http import JsonResponse
from request.config import folder_structure
from rest_framework import serializers
import json
# Create your views here.

class Transrequest(generics.CreateAPIView):
    queryset = TransRequest.objects.all()
    serializer_class = TransRequestSerailizer
    def create(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            CAFID=serializer.data.get('cafid')
            ClientID=serializer.data.get('clientid')
            ClientName=serializer.data.get('clientname')
            ClientType=serializer.data.get('clienttype')
            ClientSubType=serializer.data.get('clientsubtype')
            RequestType=serializer.data.get('requesttype')
            print(ClientName.isnumeric())
            cursor = connection.cursor()
            str_CAFID = str(CAFID)
            Clientid_name = str(ClientID)+'_'+str(ClientName)
            folderpath=folder_structure(str_CAFID, Clientid_name)

            sp = cursor.execute("set nocount on; EXEC	[dbo].[InsertNewRequest] @cafid='"+str(CAFID)+"',@clientid='"+str(ClientID)+"',@clientname='"+str(ClientName)+"',@clienttype= '"+str(ClientType)+"',@clientsubtype= '"+str(ClientSubType)+"',@requesttype='"+str(RequestType)+"',@filesharepath='"+str(folderpath)+"'")
            if ClientName.isnumeric():
                 print(ClientName.isnumeric())
                 msg = 'Client name should not have only integers'
                 raise serializers.ValidationError(msg)
            cursor.commit()
            rows = sp.fetchall()
            row_headers = [x[0] for x in cursor.description]
            json_data = []
            for result in rows:
              json_data.append(dict(zip(row_headers,result)))
            return JsonResponse(json_data[0])
        else:
            return Response("Json data is invalid")





class Transresponse(generics.RetrieveAPIView):
    queryset = TransResponse.objects.all()
    serializer_class = TransResponseSerailizer
    lookup_field = 'cafid'
    def retrieve(self, request, cafid):
        print(cafid)
        cursor = connection.cursor()
        sp = cursor.execute("set nocount on; EXEC [dbo].[SendResponse] @cafid='"+str(cafid)+"'")
        print(sp)
        row_headers = [x[0] for x in cursor.description]
        rows = sp.fetchall()
        json_data = []
        for result in rows:
            json_data.append(dict(zip(row_headers, result)))
        return JsonResponse(json_data[0])

