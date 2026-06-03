from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm, NetBoxModelBulkEditForm
from utilities.forms.fields import CommentField, TagFilterField
from utilities.forms.widgets import DatePicker
from utilities.forms.utils import add_blank_choice
from .models import Changelog, ChangelogCategoryChoices

class ChangelogForm(NetBoxModelForm):
    comments = CommentField(
        label='备注',
        required=False
    )
    description = CommentField(
        label='详细描述',
        required=False,
        help_text='支持 Markdown 格式'
    )

    class Meta:
        model = Changelog
        fields = (
            'date', 'version', 'category', 'title', 'description', 'comments', 'tags'
        )
        widgets = {
            'date': DatePicker(),
            'description': forms.Textarea(attrs={'rows': 10}),
        }

class ChangelogFilterForm(NetBoxModelFilterSetForm):
    model = Changelog
    date_after = forms.DateField(
        required=False,
        label='开始日期',
        widget=DatePicker()
    )
    date_before = forms.DateField(
        required=False,
        label='结束日期',
        widget=DatePicker()
    )
    category = forms.ChoiceField(
        choices=add_blank_choice(ChangelogCategoryChoices),
        required=False,
        label='分类'
    )
    version = forms.CharField(
        required=False,
        label='版本号'
    )
    tag = TagFilterField(Changelog)

class ChangelogImportForm(NetBoxModelImportForm):
    class Meta:
        model = Changelog
        fields = (
            'date', 'version', 'category', 'title', 'description', 'comments'
        )

class ChangelogBulkEditForm(NetBoxModelBulkEditForm):
    model = Changelog
    date = forms.DateField(
        required=False,
        label='日期',
        widget=DatePicker()
    )
    category = forms.ChoiceField(
        choices=add_blank_choice(ChangelogCategoryChoices),
        required=False,
        label='分类'
    )
    version = forms.CharField(
        required=False,
        label='版本号'
    )
    comments = CommentField(
        required=False,
        label='备注'
    )

    nullable_fields = (
        'version', 'description', 'comments'
    )
