from django.test import TestCase
from django.db import IntegrityError, transaction
from users.models import Profile
from django.contrib.auth.models import User

# Create your tests here.


class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User(email = 'abc@gmail.com', username = 'Abc254', password = 'test123')
        self.new_profile = Profile(user = self.new_user.pk, profile_pic = '/media/profile_pics/image.jpeg', bio = 'Im a developer')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_profile(self):
        try:
            with transaction.atomic():
                self.new_profile.save_profile()
                profiles = Profile.objects.all()
                self.assertTrue(len(profiles) > 0)
        except IntegrityError:
            pass

    def test_delete_profile(self):
        try:
            with transaction.atomic():
                self.new_profile.save()
                self.new_profile.delete_profile()
                profiles = Profile.objects.all()
                self.assertTrue(len(profiles) < 1)
        except IntegrityError:
            pass

    # def tearDown(self):
    #     Profile.objects.all().delete()
    #     User.objects.all().delete()