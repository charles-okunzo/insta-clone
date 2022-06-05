from PIL import Image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', default= 'default.png')
    bio = models.TextField(blank=True)


    def save(self):
        super().save()


        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)

            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls, user):
        cls.objects.filter(user__username = user)



    def __str__(self) -> str:
        return f"{self.user.username} Profile"



