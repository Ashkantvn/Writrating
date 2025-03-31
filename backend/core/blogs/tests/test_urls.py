from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blogs.api.v1 import views

class TestUrls(SimpleTestCase):

    def test_blogs_list_url_is_resolved(self):
        url = reverse('blogs:list')
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, views.BlogListAPIView)

    def test_blog_retrieve_url_is_resolved(self):
        url = reverse('blogs:details', args={'slug': 'test-blog'})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, views.BlogRetrieveAPIView)

    def test_blog_add_url_is_resolved(self):
        url = reverse('blogs:add')
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class,views.BlogAddAPIView)

    def test_blog_edit_url_is_resolved(self):
        url = reverse('blogs:edit', args={'slug': 'test-blog'})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, views.BlogEditAPIView)

    def test_blog_delete_is_resolved(self):
        url = reverse('blogs:delete', args={'slug': 'test-blog'})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, views.BlogDeleteAPIView)

    def test_blog_check_is_resolved(self):
        url = reverse('blogs:check', args={'slug': 'test-blog'})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, views.BlogCheckAPIView)