from datetime import datetime
from typing import Union

from django.db import models
from django.conf import settings


class KinveyDateField(models.DateTimeField):
    """Field to map Django model fields to text and ISO8601 encoded dates"""

    description = "Kinvey date field"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 32
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def get_prep_value(self, value):
        return value.isoformat()

    def db_type(self, connection) -> str:
        return f"char({self.max_length})"

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

    def process_to_datetime(self, value) -> Union[None, datetime]:
        return datetime.fromisoformat(value)

    def to_python(self, value) -> Union[None, datetime]:
        if isinstance(value, datetime):
            return value

        if value is None:
            return value

        return self.process_to_datetime(value)
# Create your models here.
class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class Vote(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    link = models.ForeignKey(
        'links.Link',
        related_name='votes',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def __str__(self):
        return 'Vote'


class Album(models.Model):
    name = models.CharField(max_length=100)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)


class Song(models.Model):
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Video(models.Model):
    name = models.CharField(max_length=100)
    createdAt = KinveyDateField(auto_now_add=True)
    updatedAt = KinveyDateField(auto_now=True)
