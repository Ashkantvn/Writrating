from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reviews import models
from reviews.api.v1 import serializers
from core.permissions import IsAuthenticatedAndAdmin, IsAuthor

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
        """
        POST /api/v1/reviews/

        Creates a review for a specified device, processor, graphics processor or operating system.

        :param request: The HTTP request
        :param request.data: A dictionary containing the review data
        :return: A Response object with a success message and a 201 status code
        :rtype: Response
        """
        serializer = serializers.AddReviewSerializer(data=request.data, context = {"user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data':'Review Generated Successfully'}, status=status.HTTP_201_CREATED)


class ReviewDetailsAPIView(APIView):

    def get(self, request, slug):
        """
        Retrieve a review by slug.

        This method fetches a review based on the provided slug. It checks for a review
        among device, processor, graphics processor, and operating system reviews. If a review
        is found, it is serialized and returned. If no review is found, a 404 response is returned.

        :param request: The HTTP request object.
        :param slug: The unique slug identifying the review.
        :return: A Response object containing serialized review data or a 404 error message.
        :rtype: Response
        """
        device_review = models.DeviceReview.objects.filter(slug=slug).first()
        processor_review = models.ProcessorReview.objects.filter(slug=slug).first()
        graphics_processor_review = models.GraphicsProcessorReview.objects.filter(slug=slug).first()
        operating_system_review = models.OperatingSystemReview.objects.filter(slug=slug).first()
        
        if device_review:
            serializer = serializers.DeviceReviewSerializer(device_review)
        elif processor_review:
            serializer = serializers.ProcessorReviewSerializer(processor_review)
        elif graphics_processor_review:
            serializer = serializers.GraphicsProcessorReviewSerializer(graphics_processor_review)
        elif operating_system_review:
            serializer = serializers.OperatingSystemReviewSerializer(operating_system_review)
        else:
            return Response({'detail': 'No review found'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ReviewDeleteAPIView(APIView):
    permission_classes = [IsAuthenticatedAndAdmin,IsAuthor]

    def delete(self, request, slug):
        """
        Delete a review by slug.

        This method deletes a review identified by the provided slug. It attempts to find
        the review among device, processor, graphics processor, and operating system reviews. 
        If a review is found, object-level permissions are checked, and the review is deleted. 
        If no review is found, a 404 response is returned.

        :param request: The HTTP request object.
        :param slug: The unique slug identifying the review to be deleted.
        :return: A Response object with a success message and a 204 status code if deleted, 
                or a 404 error message if no review is found.
        :rtype: Response
        """
        device_review = models.DeviceReview.objects.filter(slug=slug).first()
        processor_review = models.ProcessorReview.objects.filter(slug=slug).first()
        graphics_processor_review = models.GraphicsProcessorReview.objects.filter(slug=slug).first()
        operating_system_review = models.OperatingSystemReview.objects.filter(slug=slug).first()

        review = device_review or processor_review or graphics_processor_review or operating_system_review
        if not review:
            return Response({'detail': 'No review found'}, status=status.HTTP_404_NOT_FOUND)
        # Check obj level permission
        self.check_object_permissions(request=request, obj=review)
        
        if device_review:
            device_review.delete()
        elif processor_review:
            processor_review.delete()
        elif graphics_processor_review:
            graphics_processor_review.delete()
        else:
            operating_system_review.delete()
        
        return Response({'detail': 'Review deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class ReviewEditAPIView(APIView):
    permission_classes = [IsAuthenticatedAndAdmin,IsAuthor]


    def patch(self, request, slug):
        """
        Edit a review by slug.

        This method updates a review based on the provided slug. It checks for a review
        among device, processor, graphics processor, and operating system reviews. If a review
        is found, it is updated with the provided data and returned. If no review is found, a 404
        response is returned.

        :param request: The HTTP request object.
        :param slug: The unique slug identifying the review.
        :return: A Response object containing serialized review data or a 404 error message.
        :rtype: Response
        """
        device_review = models.DeviceReview.objects.filter(slug=slug).first()
        processor_review = models.ProcessorReview.objects.filter(slug=slug).first()
        graphics_processor_review = models.GraphicsProcessorReview.objects.filter(slug=slug).first()
        operating_system_review = models.OperatingSystemReview.objects.filter(slug=slug).first()

        review = device_review or processor_review or graphics_processor_review or operating_system_review
        if not review:
            return Response({'detail': 'No review found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Check obj level permission
        self.check_object_permissions(request=request, obj=review)

        serializer = serializers.EditReviewSerializer(partial=True,data=request.data,instance=review)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ReviewCheckAPIView(APIView):
    pass


