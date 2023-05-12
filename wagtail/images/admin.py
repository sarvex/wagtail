from django.conf import settings
from django.contrib import admin

from wagtail.images.models import Image

if (
    not hasattr(settings, "WAGTAILIMAGES_IMAGE_MODEL")
    or settings.WAGTAILIMAGES_IMAGE_MODEL == "wagtailimages.Image"
):
    admin.site.register(Image)
