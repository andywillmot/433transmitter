from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from WiringPin import WiringPin
from optparse import OptionParser
from strogonanoff_sender import send_command
from time import sleep

@api_view(['POST','GET'])
def switch_socket(request,channel,button,action):
    """
    Switch the socket
    """
    if request.method == 'POST' or request.method == 'GET':
        print ("Got a hit! Channel:%s Button:%s Action:%s") % (channel,button,action)

        actionBool = True if action.upper()=="ON" else False
        pin = WiringPin(3).export()
        sleep(1)
        for i in range(1, 10):
            send_command(pin,int(channel),int(button),actionBool)

#             send_command(pin,1,1,True)
        return Response(status=status.HTTP_200_OK)




# Create your views here.
