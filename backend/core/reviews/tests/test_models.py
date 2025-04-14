import pytest
from reviews.tests.fixtures import graphic_processor_review,device_review,processor_review,operating_system_review


@pytest.mark.django_db
class TestReviewModels:
    def test_create_device_review_model(self,device_review):
        assert device_review.pk
        assert device_review.target
        assert device_review.author
        
    def test_create_processor_review_model(self,processor_review):
        assert processor_review.pk
        assert processor_review.target
        assert processor_review.author
    
    def test_create_graphic_processor_review_model(self,graphic_processor_review):
        assert graphic_processor_review.pk
        assert graphic_processor_review.target
        assert graphic_processor_review.author
    
    def test_create_operating_system_review_model(self,operating_system_review):
        assert operating_system_review.pk
        assert operating_system_review.target
        assert operating_system_review.author

    def test_str_representation(self,device_review,processor_review,graphic_processor_review,operating_system_review):
        assert str(device_review) == f"{device_review.target.device_name} Review"
        assert str(processor_review) == f"{processor_review.target.processor_name} Review"
        assert str(graphic_processor_review) == f"{graphic_processor_review.target.graphic_processor_name} Review"
        assert str(operating_system_review) == f"{operating_system_review.target.os_name} Review"
        
    def test_auto_generated_fields(self,device_review,processor_review,graphic_processor_review,operating_system_review):
        assert device_review.created_date
        assert processor_review.created_date
        assert graphic_processor_review.created_date
        assert operating_system_review.created_date

        assert device_review.updated_date
        assert processor_review.updated_date
        assert graphic_processor_review.updated_date
        assert operating_system_review.updated_date

        assert device_review.slug
        assert processor_review.slug
        assert graphic_processor_review.slug
        assert operating_system_review.slug