from django.db import models
from helpers.models import BaseModel
from common.models import User
from post.models import Post

post_type_choices = (
    ("public", "public"),
    ("friends", "friends"),
    ("private", "only me")
)


class Chat(BaseModel):
    members = models.ManyToManyField(User, related_name='enrolled_chats')


# Create your models here.
class Message(BaseModel):
    post_type = models.CharField(choices=post_type_choices)
    text = models.TextField()
    image = models.ImageField(upload_to="/media/post", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")


class Comment(BaseModel):
    text = models.TextField()
    image = models.ImageField(upload_to="/media/comment/", blank=True, null=True)
    author = models.ForeignKey(User, related_name="user_comments", on_delete=models.DO_NOTHING)
    related_post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)


