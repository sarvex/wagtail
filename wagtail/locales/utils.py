from wagtail.models import Page, get_translatable_models


def get_locale_usage(locale):
    """
    Returns the number of pages and other objects that use a locale
    """
    num_pages = Page.objects.filter(locale=locale).exclude(depth=1).count()

    num_others = sum(
        model.objects.filter(locale=locale).count()
        for model in get_translatable_models()
        if model is not Page
    )
    return num_pages, num_others
