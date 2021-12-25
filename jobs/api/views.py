from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from jobs.models import JobOffer
from jobs.api.serializers import JobOfferSerializer


class JobOfferListCreateAPIView(APIView):

    def get(self, request):
        offers = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(offers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class JobOfferDetailAPIView(APIView):

    def get_object(self, pk):
        offer = get_object_or_404(JobOffer, pk=pk)
        return offer
    
    def get(self, request, pk):
        offer = self.get_object(pk)
        serializer = JobOfferSerializer(offer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        offer = self.get_object(pk)
        serializer = JobOfferSerializer(offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def delete(self, request, pk):
        offer = self.get_object(pk)
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)