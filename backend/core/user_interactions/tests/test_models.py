import pytest
from user_interactions import models
from user_interactions.tests.fixtures import report

@pytest.mark.django_db
class TestInteractionsModels:

    def test_report_model_is_created(self,report):
        assert report.pk
        assert report.report_title
        assert report.report_content

    def test_str_representation(self,report):
        assert str(report) == report.report_title

    def test_auto_create_fields(self,report):
        assert report.created_date
        assert report.updated_date

