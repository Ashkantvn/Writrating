from rest_framework import serializers
from reviews import models


class DeviceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceReview
        exclude = ['status','publishable','created_date','updated_date']


class ProcessorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProcessorReview
        exclude = ['status','publishable','created_date','updated_date']

class OperatingSystemReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OperatingSystemReview
        exclude = ['status','publishable','created_date','updated_date']

class GraphicsProcessorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GraphicsProcessorReview
        exclude = ['status','publishable','created_date','updated_date']

