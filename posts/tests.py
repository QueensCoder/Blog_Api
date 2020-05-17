from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        post = Post.objects.create(
            title='first title', body='test body', author=user)
        post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        self.assertEquals(f'{post.title}', 'first title')
        self.assertEquals(f'{post.author.username}', 'john')
        self.assertEquals(f'{post.author.email}', 'lennon@thebeatles.com')
        self.assertEquals(f'{post.body}', 'test body')

    # def test_title(self):
    #     post = Post.objects.get(id=1)
    #     self.assertEquals(f'{post.title}', 'first title')

    # def test_author(self):
    #     post = Post.objects.get(id=1)
    #     self.assertEquals(f'{post.author.username}', 'john')
    #     self.assertEquals(f'{post.author.email}', 'lennon@thebeatles.com')

    # def test_body(self):
    #     post = Post.objects.get(id=1)
    #     self.assertEquals(f'{post.body}', 'test body')
