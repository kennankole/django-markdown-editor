from django.test import TestCase
from . import models

class PostTestCase(TestCase):
    def testPost(self):
        post = models.Post(title="My Title", description="Blurb", wiki="Post Body")
        self.assertEqual(post.title, "My Title")
        self.assertEqual(post.description, "Blurb")
        self.assertEqual(post.wiki, "Post Body")

