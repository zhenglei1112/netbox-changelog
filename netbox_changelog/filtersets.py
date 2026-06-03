from django.db.models import Q, QuerySet
import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from .models import Changelog

class ChangelogFilterSet(NetBoxModelFilterSet):
    date_after = django_filters.DateFilter(
        field_name='date', lookup_expr='gte'
    )
    date_before = django_filters.DateFilter(
        field_name='date', lookup_expr='lte'
    )

    class Meta:
        model = Changelog
        fields = ('id', 'date', 'version', 'category', 'title')

    def search(self, queryset: QuerySet, name: str, value: str) -> QuerySet:
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(title__icontains=value)
            | Q(version__icontains=value)
            | Q(description__icontains=value)
            | Q(comments__icontains=value)
        ).distinct()
