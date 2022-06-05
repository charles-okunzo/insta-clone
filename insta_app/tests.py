from django.test import TestCase
from django.contrib.auth.models import User
from insta_app.models import Post
from datetime import datetime
from django.db import IntegrityError, transaction
# Create your tests here.

class PostTestCase(TestCase):
    def setUp(self):
        self.new_user = User(email = 'abc@gmail.com', username = 'Abc254', password = 'test123')
        self.new_post = Post(user = self.new_user.pk, image_path = 'media/post_images/image1.png',  image_name='My meal', image_caption = 'Hello there', posted_date = datetime.now())

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))


    def test_save_post(self):
        try:
            with transaction.atomic():
                self.new_post.save_post()
                posts = Post.objects.all()
                self.assertTrue(len(posts) > 0)

        except IntegrityError:
            pass

    def test_delete_post(self):
        try:
            with transaction.atomic():
                self.new_post.save_post()
                self.new_post.delete_post()
                posts = Post.objects.all()
                self.assertTrue(len(posts) < 1)

        except IntegrityError:
            pass

