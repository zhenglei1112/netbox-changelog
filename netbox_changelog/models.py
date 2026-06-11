from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
import taggit.managers

class ChangelogCategoryChoices(ChoiceSet):
    key = 'Changelog.category'

    FEATURE = 'feature'
    FIX = 'fix'
    UPGRADE = 'upgrade'
    MAINTENANCE = 'maintenance'
    SECURITY = 'security'
    OTHER = 'other'

    CHOICES = [
        (FEATURE, '新功能', 'green'),
        (FIX, '问题修复', 'red'),
        (UPGRADE, '系统升级', 'blue'),
        (MAINTENANCE, '日常维护', 'orange'),
        (SECURITY, '安全更新', 'purple'),
        (OTHER, '其他变更', 'gray'),
    ]

class Changelog(NetBoxModel):
    date = models.DateField(
        verbose_name='日期'
    )
    version = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='版本号',
        help_text='例如 v1.0.0'
    )
    category = models.CharField(
        max_length=50,
        choices=ChangelogCategoryChoices,
        default=ChangelogCategoryChoices.OTHER,
        verbose_name='分类'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='标题'
    )
    description = models.TextField(
        blank=True,
        verbose_name='详细描述',
        help_text='支持 Markdown 格式'
    )
    comments = models.TextField(
        blank=True,
        verbose_name='备注'
    )
    tags = taggit.managers.TaggableManager(
        through='extras.TaggedItem',
        to='extras.Tag',
        blank=True
    )

    class Meta:
        ordering = ('-date', '-pk')
        verbose_name = '更新日志'
        verbose_name_plural = '更新日志'

    def __str__(self) -> str:
        if self.version:
            return f"[{self.version}] {self.title}"
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('plugins:netbox_changelog:changelog', args=[self.pk])

    def get_category_color(self) -> str | None:
        return ChangelogCategoryChoices.colors.get(self.category)

    def get_category_icon(self) -> str:
        icons = {
            'feature': 'mdi-star-outline',
            'fix': 'mdi-bug-outline',
            'upgrade': 'mdi-arrow-up-bold-circle-outline',
            'maintenance': 'mdi-cog-outline',
            'security': 'mdi-shield-check-outline',
            'other': 'mdi-tag-outline',
        }
        return icons.get(self.category, 'mdi-tag-outline')
