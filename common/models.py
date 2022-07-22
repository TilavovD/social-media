# from django.conf import settings
from django.contrib.auth.models import AbstractUser
from helpers.models import BaseModel

from django.db import models
from post.models import Post

class User(AbstractUser):
    INVALID_CODE = "######"

    full_name = models.CharField(("full name"), max_length=256)
    email = models.EmailField(
        ("email"),
        unique=True,
        error_messages={
            "error": ("Bunday email mavjud."),
        },
        null=True
    )
    avatar = models.ImageField(upload_to="avatar")
    followers = models.ManyToManyField('self', blank=True, null=True)
    followings = models.ManyToManyField('self', blank=True, null=True)
    
    followers_count = models.PositiveIntegerField("followers count", default=0)
    followings_count = models.PositiveIntegerField("followings count", default=0)
    
    # SETTINGS
    USERNAME_FIELD = "email"
    first_name = None
    last_name = None
    REQUIRED_FIELDS = ["username", "full_name"]

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = ("user")
        verbose_name_plural = ("users")

    def follow(self, user_on_page):
        self.followings.add(user_on_page)
        user_on_page.followers.add(self)
        self.followings_count += 1
        user_on_page.followers_count += 1

    def unfollow(self, followed_user):
        self.followers.remove(followed_user)
        followed_user.followings.remove(self)
        self.followings_count -= 1
        followed_user.followers_count -= 1


class Comment(BaseModel):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

class SubscribeForm(models.Model):
    email = models.EmailField()
    