from django.core.exceptions import PermissionDenied

from wagtail.log_actions import log


class DeletePagePermissionError(PermissionDenied):
    """
    Raised when the page delete cannot be performed due to insufficient permissions.
    """

    pass


class DeletePageAction:
    def __init__(self, page, user):
        self.page = page
        self.user = user

    def check(self, skip_permission_checks=False):
        if (
            self.user
            and not skip_permission_checks
            and not self.page.permissions_for_user(self.user).can_delete()
        ):
            raise DeletePagePermissionError(
                "You do not have permission to delete this page"
            )

    def _delete_page(self, page, *args, **kwargs):
        from wagtail.models import Page

        if type(page) is not Page:
            # retrieve an actual Page instance and delete that instead of page
            return DeletePageAction(
                Page.objects.get(id=page.id), user=self.user
            ).execute(*args, **kwargs)
        for child in page.get_descendants().specific().iterator():
            self.log_deletion(child)
        self.log_deletion(page.specific)

        # this is a Page instance, so carry on as we were
        return super(Page, page).delete(*args, **kwargs)

    def execute(self, *args, skip_permission_checks=False, **kwargs):
        self.check(skip_permission_checks=skip_permission_checks)

        return self._delete_page(self.page, *args, **kwargs)

    def log_deletion(self, page):
        log(
            instance=page,
            action="wagtail.delete",
            user=self.user,
            deleted=True,
        )
