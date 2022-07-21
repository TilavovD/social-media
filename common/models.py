# from django.conf import settings
from django.contrib.auth.models import AbstractUser
from helpers.models import BaseModel

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# from django.utils import timezone
genders = (
    ("M", "male"),
    ("F", "female"),
)


class Language(BaseModel):
    name = models.CharField(max_length=128)
    acronym = models.CharField(max_length=128)


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
    gender = models.CharField(choices=genders, max_length=128)
    location = models.CharField(max_length=128)
    born_year = models.DateTimeField("born year", null=True)
    phone_number = models.PositiveIntegerField("phone_number", null=True)
    bio = models.TextField()
    website = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to="avatar")
    cover_photo = models.ImageField(upload_to="cover")

    followers = models.ManyToManyField('self', blank=True, null=True)
    followings = models.ManyToManyField('self', blank=True, null=True)
    blocked_users = models.ManyToManyField('self', blank=True, null=True)

    twitter_link = models.CharField(max_length=128, blank=True, default="")
    instagram_link = models.CharField(max_length=128, blank=True, default="")
    facebook_link = models.CharField(max_length=128, blank=True, default="")
    linkedin_link = models.CharField(max_length=128, blank=True, default="")

    followers_count = models.PositiveIntegerField("followers count", default=0)
    followings_count = models.PositiveIntegerField("followings count", default=0)
    blocked_users_count = models.PositiveIntegerField("blocked users count", default=0)

    created_at = models.DateTimeField("date created", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("date updated", auto_now=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)

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


