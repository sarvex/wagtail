from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def cell_classname(context, row_index, col_index, table_header=None):
    if classnames := context.get("classnames"):
        if table_header is not None:
            row_index += 1
        index = (row_index, col_index)
        if cell_class := classnames.get(index):
            return mark_safe(f'class="{cell_class}"')
    return ""
