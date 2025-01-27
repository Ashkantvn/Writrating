import pytest
from blogs.models.blogs_model import Blog

@pytest.mark.django_db
class TestBlogModel:

    def test_blog_creation(self):
        pass
    
    def test_fields_defaults(self):
        pass

    def test_title_field_max_length(self):
        pass

    def test_fields_not_blank_or_null(self):
        pass

    def test_str_representation(self):
        pass

    def test_foreign_key_relationship(self):
        pass

    def test_many_to_many_relationship(self):
        pass