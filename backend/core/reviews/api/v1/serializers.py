from rest_framework import serializers , exceptions
from reviews import models
from django.core.validators import MinValueValidator, MaxValueValidator
from devices import models as DeviceModels
from accounts import models as AccountModels

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

class AddReviewSerializer(serializers.Serializer):
    review_title = serializers.CharField()
    review_text = serializers.CharField()
    rating = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    buying_worth = serializers.CharField()
    published_date = serializers.DateField()
    target = serializers.CharField()
    target_type = serializers.ChoiceField(choices=["Device", "Processor", "GraphicsProcessor", "OperatingSystem"])

    def validate(self, attrs):
        target = attrs.get('target')
        target_type = attrs.get('target_type')

        if target_type == "Device" and not DeviceModels.Device.objects.filter(slug=target).exists():
            raise exceptions.NotFound("Device does not exist")
        elif target_type == "Processor" and not DeviceModels.Processor.objects.filter(slug=target).exists():
            raise exceptions.NotFound("Processor does not exist")
        elif target_type == "GraphicsProcessor" and not DeviceModels.GraphicProcessor.objects.filter(slug=target).exists():
            raise exceptions.NotFound("GraphicsProcessor does not exist")
        elif target_type == "OperatingSystem" and not DeviceModels.OperatingSystem.objects.filter(slug=target).exists():
            raise exceptions.NotFound("OperatingSystem does not exist")
        else:
            return super().validate(attrs)
        

    def create(self, validated_data):
        target_type = validated_data.pop("target_type")
        slug = validated_data.pop("target")

        # set author
        user = self.context.get("user")
        if not user:
            raise serializers.ValidationError(
                detail="A valid user profile is required to create a review."
            )
        else:
            author = AccountModels.Profile.objects.get(user=user)
            validated_data["author"] = author

        # set target
        if target_type == "Device":
            target = DeviceModels.Device.objects.get(slug=slug)
            if target.pk:
                validated_data["target"] = target
                return models.DeviceReview.objects.create(**validated_data)
        elif target_type == "Processor":
            target = DeviceModels.Processor.objects.get(slug=slug)
            if target.pk:
                validated_data["target"] = target
                return models.ProcessorReview.objects.create(**validated_data)
        elif target_type == "GraphicsProcessor":
            target = DeviceModels.GraphicProcessor.objects.get(slug=slug)
            if target.pk:
                validated_data["target"] = target
                return models.GraphicsProcessorReview.objects.create(**validated_data)
        elif target_type == "OperatingSystem":
            target = DeviceModels.OperatingSystem.objects.get(slug=slug)
            if target.pk:
                validated_data["target"] = target
                return models.OperatingSystemReview.objects.create(**validated_data)

class EditReviewSerializer(serializers.Serializer):
    review_text = serializers.CharField()
    rating = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    buying_worth = serializers.CharField()
    published_date = serializers.DateField()
    status = serializers.CharField()

    def update(self, instance, validated_data):
        instance.review_text = validated_data.get('review_text',instance.review_text)
        instance.rating = validated_data.get('rating',instance.rating)
        instance.published_date = validated_data.get('published_date',instance.published_date)
        instance.buying_worth = validated_data.get('buying_worth',instance.buying_worth)
        instance.status = validated_data.get('status',instance.status)

        instance.save()

        return instance
