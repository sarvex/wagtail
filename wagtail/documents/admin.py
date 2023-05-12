from django.conf import settings
from django.contrib import admin

from wagtail.documents.models import Document

if (
    not hasattr(settings, "WAGTAILDOCS_DOCUMENT_MODEL")
    or settings.WAGTAILDOCS_DOCUMENT_MODEL == "wagtaildocs.Document"
):
    admin.site.register(Document)
