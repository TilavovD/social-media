from django.db import models
from helpers.models import BaseModel
from common.models import User

class Tag(BaseModel):
    name = models.CharField(max_length=128)
    posts_count = models.PositiveIntegerField(default=0)

# Create your models here.
class Post(BaseModel):
    title = models.CharField(max_length=128)
    content = models.TextField()
    content = models.TextField()

    image = models.ImageField(upload_to="post")
    image_title = models.CharField(max_length=128, default="", blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    views_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, on_delete=models.SET_NULL, related_name="posts")

    reading_minutes = models.PositiveIntegerField(default=0)