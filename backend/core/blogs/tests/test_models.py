import pytest
from blogs.tests.fixtures import blog, blog_with_more_than_60_characters,blog_with_blank_fields
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from blogs.models import Blog,Tag,Category

User = get_user_model()

@pytest.mark.django_db
class TestBlogModel:

    def test_blog_creation(self,blog):
        assert blog.pk
        assert blog.title == 'Test Blog'
        assert blog.banner
        assert blog.status == False
        assert blog.views == 0
        assert blog.slug == 'test-blog'
        assert blog.publishable == False
        assert blog.published_date
        assert blog.create_date
        assert blog.update_date

    def test_title_field_max_length(self,blog_with_more_than_60_characters):
        with pytest.raises(ValidationError) as exc:
            blog_with_more_than_60_characters.full_clean()
        assert 'title' in exc.value.message_dict


    def test_fields_blank_or_null(selfm,blog_with_blank_fields):
        with pytest.raises(ValidationError) as exc:
            blog_with_blank_fields.full_clean()
        assert 'title' in exc.value.message_dict
        assert 'content' in exc.value.message_dict

    def test_str_representation(self,blog):
        assert str(blog) == 'Test Blog'

    def test_foreign_key_relationship(self,blog):
        assert blog.author
        assert isinstance(blog.author,User)
        assert blog.author.email == 'test323123@example.com'

        another_blog = Blog.objects.create(
            title='Other Blog',
            content='Other Content',
            author=blog.author
        )

        author_blogs = blog.author.blog_set.all()

        # Ensure that the author of the blog is the same as the author of the other blog
        assert another_blog.author == blog.author

        # Ensure that the author has both blogs
        assert (another_blog in author_blogs) and (blog in author_blogs)
        

    def test_many_to_many_relationship(self,blog):
        tag1 = Tag.objects.create(name='tag1')
        tag2 = Tag.objects.create(name='tag2')
        category1 = Category.objects.create(name='category1')
        category2 = Category.objects.create(name='category2')

        # Ensure that the tags are added to the blog
        blog.tags.add(tag1,tag2)
        assert blog.tags.count() == 2
        assert tag1 in blog.tags.all()
        assert tag2 in blog.tags.all()

        # Remove tag from the blog
        blog.tags.remove(tag1)
        assert blog.tags.count() == 1
        assert tag1 not in blog.tags.all()
        assert tag1 in Tag.objects.all()

        # Ensure that the categories are added to the blog
        blog.categories.add(category1,category2)
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

        
