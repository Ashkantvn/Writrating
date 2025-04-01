import pytest
from blogs.tests.fixtures import (
    blog,
    blog_with_more_than_60_characters,
    blog_with_blank_fields,
    blog_response,
)
from django.core.exceptions import ValidationError
from blogs.models import Blog, Tag, Category
from accounts.models import Profile


@pytest.mark.django_db
class TestBlogModel:

    def test_blog_creation(self, blog):
        assert blog.pk
        assert blog.title == "Test Blog"
        assert blog.banner
        assert not blog.status
        assert blog.views == 0
        assert blog.slug == "test-blog"
        assert not blog.publishable
        assert blog.published_date
        assert blog.create_date
        assert blog.update_date

    def test_title_field_max_length(self, blog_with_more_than_60_characters):
        with pytest.raises(ValidationError) as exc:
            blog_with_more_than_60_characters.full_clean()
        assert "title" in exc.value.message_dict

    def test_fields_blank_or_null(self, blog_with_blank_fields):
        with pytest.raises(ValidationError) as exc:
            blog_with_blank_fields.full_clean()
        assert "title" in exc.value.message_dict
        assert "content" in exc.value.message_dict

    def test_str_representation(self, blog):
        assert str(blog) == "Test Blog"

    def test_foreign_key_relationship(self, blog):
        assert blog.author
        assert isinstance(blog.author, Profile)

        another_blog = Blog.objects.create(
            title="Other Blog", content="Other Content", author=blog.author
        )

        author_blogs = blog.author.blog_set.all()

        # Ensure that the author of the blog is the same as the author of the other blog
        assert another_blog.author == blog.author

        # Ensure that the author has both blogs
        assert (another_blog in author_blogs) and (blog in author_blogs)

    def test_many_to_many_relationship(self, blog):
        tag1 = Tag.objects.create(name="tag1")
        tag2 = Tag.objects.create(name="tag2")
        category1 = Category.objects.create(name="category1")
        category2 = Category.objects.create(name="category2")

        # Ensure that the tags are added to the blog
        blog.tags.add(tag1, tag2)
        assert blog.tags.count() == 2
        assert tag1 in blog.tags.all()
        assert tag2 in blog.tags.all()

        # Remove tag from the blog
        blog.tags.remove(tag1)
        assert blog.tags.count() == 1
        assert tag1 not in blog.tags.all()
        assert tag1 in Tag.objects.all()

        # Ensure that the categories are added to the blog
        blog.categories.add(category1, category2)
        assert blog.categories.count() == 2
        assert category1 in blog.categories.all()
        assert category2 in blog.categories.all()

        # Remove category from the blog
        blog.categories.remove(category1)
        assert blog.categories.count() == 1
        assert category1 not in blog.categories.all()
        assert category1 in Category.objects.all()

        # Ensure that the tags and categories are not deleted when the blog is deleted
        blog.delete()
        assert tag2 in Tag.objects.all()
        assert category2 in Category.objects.all()


@pytest.mark.django_db
class TestCategoryModel:

    def test_category_creation(self):
        category = Category.objects.create(name="Test Category")
        assert category.pk
        assert category.name == "Test Category"
        assert category.created_date
        assert category.updated_date

    def test_name_field_max_length(self):
        with pytest.raises(ValidationError) as exc:
            Category.objects.create(name="a" * 61).full_clean()
        assert "name" in exc.value.message_dict

    def test_str_representation(self):
        category = Category.objects.create(name="Test Category")
        assert str(category) == "Test Category"


@pytest.mark.django_db
class TestTagModel:

    def test_tag_creation(self):
        tag = Tag.objects.create(name="Test Tag")
        assert tag.pk
        assert tag.name == "Test Tag"
        assert tag.created_date
        assert tag.updated_date

    def test_name_field_max_length(self):
        with pytest.raises(ValidationError) as exc:
            Tag.objects.create(name="a" * 61).full_clean()
        assert "name" in exc.value.message_dict

    def test_str_representation(self):
        tag = Tag.objects.create(name="Test Tag")
        assert str(tag) == "Test Tag"


@pytest.mark.django_db
class TestBlogResponseModel:

    def test_blog_response_creation(self, blog_response):
        assert blog_response.pk
        assert blog_response.response_to
        assert blog_response.content
        assert blog_response.author

    def test_blog_response_str_representation(self, blog_response):
        assert (
            str(blog_response)
            == f"Blog Response to {blog_response.response_to} by {blog_response.author.username}"
        )

    def test_blog_response_foreign_key_relationship(self, blog_response):
        assert blog_response.response_to
        assert isinstance(blog_response.response_to, Profile)
        assert blog_response.author
        assert isinstance(blog_response.author, Profile)
