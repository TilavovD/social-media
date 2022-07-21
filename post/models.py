from django.db import models
from helpers.models import BaseModel
from common.models import User

post_type_choices = (
    ("public", "public"),
    ("friends", "friends"),
    ("private", "only me")
)


# Create your models here.
class Post(BaseModel):
    content = models.TextField()
    image = models.ImageField(upload_to="/media/post")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_type = models.CharField(choices=post_type_choices)

    comments_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    dislikes_count = models.PositiveIntegerField(default=0)
    shares_count = models.PositiveIntegerField(default=0)

    users_like = models.ManyToManyField(User, related_name="posts_liked", blank=True)

    def like_add(self, post):
        post.likes_count += 1

    def dislike_add(self, post):
        post.likes_count -= 1


