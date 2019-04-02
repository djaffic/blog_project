from django.test import TestCase, Client
from django.urls import reverse

from .models import Post, Category


class SimpleTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.category = Category.objects.create(name="Test", slug="test")
        self.post = Post.objects.create(
            title="Post test",
            text="Test text",
            slug="post-test",
            category=self.category
        )

    def test_category(self):
        self.assertEqual(self.category.slug, "test")

    def test_post(self):
        self.assertEqual(self.post.title, "Post test")

    def test_list_post(self):
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)

    def test_post_single(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_post_single_response(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.context.get("post").text, "Test text")