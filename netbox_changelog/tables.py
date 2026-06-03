import django_tables2 as tables
from django.utils.html import format_html
from django.utils.safestring import SafeString
from netbox.tables import NetBoxTable, columns
from .models import Changelog

class ChangelogTable(NetBoxTable):
    title = tables.Column(
        linkify=True,
        verbose_name='标题'
    )
    category = columns.ChoiceFieldColumn(
        verbose_name='分类'
    )
    version = tables.Column(
        verbose_name='版本号'
    )
    date = tables.DateColumn(
        format='Y-m-d',
        verbose_name='日期'
    )
    tags = columns.TagColumn(
        url_name='plugins:netbox_changelog:changelog_list'
    )

    class Meta(NetBoxTable.Meta):
        model = Changelog
        fields = (
            'pk', 'id', 'date', 'version', 'category', 'title', 'comments', 'tags', 'actions',
        )
        default_columns = (
            'date', 'version', 'category', 'title', 'tags',
        )

    def render_category(self, value: str, record: Changelog) -> SafeString:
        color = record.get_category_color()
        return format_html('<span class="badge bg-{} text-white">{}</span>', color, record.get_category_display())

    def value_category(self, value: str, record: Changelog) -> str:
        return record.get_category_display() or ''
