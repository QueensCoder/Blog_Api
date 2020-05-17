from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        post = Post.objects.create(
            title='first title', body='test body', author=user)

    def test_title(self):
        post = Post.objects.get(id=1)
        self.assertEquals(f'{post.title}', 'first title')

    def test_author(self):
        post = Post.objects.get(id=1)
        self.assertEquals(f'{post.author.username}', 'john')
        self.assertEquals(f'{post.author.email}', 'lennon@thebeatles.com')

    def test_body(self):
        post = Post.objects.get(id=1)
        self.assertEquals(f'{post.body}', 'test body')
