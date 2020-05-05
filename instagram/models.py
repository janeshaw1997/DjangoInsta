from django.db import models

from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField

from django.urls import reverse

# Create your models here.

class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        options = {'quality': 100},
        blank = True,
        null = True
    )

    def get_connections(self):
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()


class UserConnection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friendship_creator_set")
    following = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friend_set")

    def __str__(self):
        return self.creator.username + ' follows ' + self.following.username

class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality': 100},
        blank = True,
        null = True
    )
    author = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='my_posts'
    )

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)]) # reverse: get the url of detail post. Reverse means turn web page into url

    def get_like_count(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='likes')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE, # if post is deleted, delete row in like table
        related_name='likes') # user1 'likes' post1, 'post1.likes' will return all rows(like objects) that contain post1

    class Meta: # define unique
        unique_together = ("post", "user") # "post + user" should be unique

    def __str__(self):
        return 'Like: ' + self.user.username + ' likes ' + self.post.title
