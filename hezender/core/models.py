from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel

"""
TODO:

- blog (list of posts and post detail)
- events
"""


class BlogModel(TimeStampedModel, TitleDescriptionModel):
    """Blog Model"""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField("TagModel", blank=True)
    category = models.ManyToManyField("CategoryModel", blank=True)
    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:blog_detail", kwargs={"slug": self.slug})


class TagModel(TitleDescriptionModel):
    """Tag Model"""

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.title


class CategoryModel(TimeStampedModel, TitleDescriptionModel):
    """Category Model"""

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class EventModel(TimeStampedModel, TitleDescriptionModel):
    """Event Model"""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    open = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.title
