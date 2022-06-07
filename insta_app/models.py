from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image_path = models.ImageField(upload_to='post_images/')
    image_name = models.CharField(max_length=20, blank=True)
    image_caption = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True, null=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)


    def save_post(self):
        self.save()

    def total_likes(self):
        return self.likes.count()


    def delete_post(self):
        self.delete()
    @classmethod
    def update_caption(cls, image_caption):
        cls.objects.filter(image_caption = image_caption)

    def __str__(self) -> str:
        return f"{self.image_name}"

    @classmethod
    def search_by_name(cls, search_term):
        serached_posts = cls.objects.filter(user__username__icontains = search_term)
        return serached_posts

    def get_absolute_url(self):
        ...


class Comment(models.Model):
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    posted_date = models.DateTimeField(auto_now_add=True, null=True)




    def __str__(self) -> str:
        return f"{self.content}"


# class Like(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


#     def __str__(self) -> str:
#         return f"{self.user.username} Likes"


#Create followers and follow
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', null=True)
    followers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers', null=True)

    def __str__(self) -> str:
        return f"{self.follower}"




