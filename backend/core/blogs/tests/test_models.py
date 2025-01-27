import pytest
from blogs.tests.fixtures import blog

@pytest.mark.django_db
class TestBlogModel:

    def test_blog_creation(self,blog):
        assert blog.title == 'Test Blog'
        assert blog.banner
        assert blog.status == False
        assert blog.views == 0
        assert blog.slug == 'test-blog'
        assert blog.publishable == False
        assert blog.published_date
        assert blog.create_date
        assert blog.update_date

    def test_title_field_max_length(self):
        pass

    def test_fields_not_blank_or_null(self):
        pass

    def test_str_representation(self,blog):
        assert str(blog) == 'Test Blog'

    def test_foreign_key_relationship(self):
        pass

    def test_many_to_many_relationship(self):
        pass