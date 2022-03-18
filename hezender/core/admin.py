from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin

from hezender.core.models import BlogModel, CategoryModel, EventModel, TagModel

# image preview in admi


# Register your models here.
@admin.register(BlogModel)
class BlogModelAdmin(SummernoteModelAdmin):
    list_display = [
        "title",
        "author",
        "created",
    ]
    list_filter = [
        "title",
        "author",
        "created",
    ]
    search_fields = [
        "title",
        "author",
        "created",
    ]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content", "description")

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        ordering = ["-created"]

    def image_tag(self, obj):
        return format_html(
            '<img src="{url}" width="{width}" height="{height}" />'.format(
                url=obj.image.url,
                width=obj.image.width,
                height=obj.image.height,
            )
        )

    image_tag.short_description = _("Image")


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ["-created"]


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created",
    ]
    list_filter = [
        "title",
        "created",
    ]
    search_fields = [
        "title",
        "created",
    ]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["-created"]


@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created",
    ]
    list_filter = [
        "title",
        "created",
    ]
    search_fields = [
        "title",
        "created",
    ]

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ["-created"]
