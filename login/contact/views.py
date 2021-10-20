from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView 
from .models import Contact
from .serializers import ContactSerializer

class ContactAPIView(APIView):
    def get(self, request, format=None):
        contact=Contact.objects.all()
        serializer=ContactSerializer(contact,many=True)
        return Response(serializer.data)
    def post(self, request):
        # contact=Contact.objects.all()
        # serializer=ContactSerializer(contact,many=True)
        # return Response(serializer.data)
        data = request.data
        serializer=ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


