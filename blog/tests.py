import datetime
from django.test import TestCase
from blog.models import Post, Comment


class BlogTestCase(TestCase):
    def test_create_post_1(self):
        self.assertEquals(0, Post.objects.count())

        p = Post()
        p.title = "Hello"
        p.content = "xyz"
        p.pub_date = datetime.datetime.today()
        p.save()

        self.assertTrue(p.id)
        self.assertEquals(1, Post.objects.count())

    def test_create_post_2(self):
        self.assertEquals(0, Post.objects.count())

        p = Post(title="Hello", content="xyz",
                 pub_date=datetime.datetime.today())
        p.save()

        self.assertTrue(p.id)
        self.assertEquals(1, Post.objects.count())

    def test_create_post_3(self):
        self.assertEquals(0, Post.objects.count())

        p = Post.objects.create(title="Hello", content="xyz",
                                pub_date=datetime.datetime.today())

        self.assertTrue(p.id)
        self.assertEquals(1, Post.objects.count())

    def create_post(self):
        return Post.objects.create(title="Hello", content="xyz",
                                pub_date=datetime.datetime.today())

    def test_create_comments(self):
        p = self.create_post()

        l = []

        c = Comment()
        c.post = p
        c.cotent = "foo"
        c.rating = 9
        c.save()

        l.append(c)
        self.assertEquals(len(l), p.comments.count())

        c = Comment.objects.create(post=p, content="blah", rating=6)

        l.append(c)
        self.assertEquals(len(l), p.comments.count())




