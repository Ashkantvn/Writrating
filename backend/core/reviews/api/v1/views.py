from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reviews import models
from reviews.api.v1 import serializers
from core.permissions import IsAuthenticatedAndAdmin

class ReviewsListAPIView(APIView):
    
    def get(self,request):
        """
        GET /api/v1/reviews/

        Returns all the reviews which are published by creator and checked by validators.

        :return: A dictionary with four keys: device_reviews, graphics_processor_reviews, processor_reviews, operating_system_reviews.
                Each key maps to a list of dictionaries where each dictionary is a review.
        :rtype: Response
        """
        
        # Get all the reviews
        devices_reviews = models.DeviceReview.objects.filter(status=True,publishable=True)
        graphic_processor_reviews = models.GraphicsProcessorReview.objects.filter(status=True,publishable=True)
        processor_reviews = models.ProcessorReview.objects.filter(status=True,publishable=True)
        operating_system_reviews = models.OperatingSystemReview.objects.filter(status=True,publishable=True)

        # Use data in a serializer
        devices_serializer = serializers.DeviceReviewSerializer(devices_reviews, many=True)
        graphic_processor_serializer = serializers.GraphicsProcessorReviewSerializer(graphic_processor_reviews, many=True)
        processor_serializer = serializers.ProcessorReviewSerializer(processor_reviews, many=True)
        operating_system_serializer = serializers.OperatingSystemReviewSerializer(operating_system_reviews, many=True)

        reviews_data = {
            'device_reviews': devices_serializer.data,
            'graphics_processor_reviews': graphic_processor_serializer.data,
            'processor_reviews': processor_serializer.data,
            'operating_system_reviews': operating_system_serializer.data,
        }

        return Response(reviews_data, status=status.HTTP_200_OK)


class ReviewAddAPIView(APIView):
    permission_classes = [IsAuthenticatedAndAdmin]

    def post(self, request):
        serializer = serializers.AddReviewSerializer(data=request.data, context = {"user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data':'Review Generated Successfully'}, status=status.HTTP_201_CREATED)