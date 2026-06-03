from netbox.views import generic
from utilities.views import register_model_view
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.db.models import Model
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from typing import Any
from .models import Changelog
from .forms import ChangelogForm, ChangelogFilterForm, ChangelogImportForm, ChangelogBulkEditForm
from .filtersets import ChangelogFilterSet
from .tables import ChangelogTable

class ChangelogReleasesView(LoginRequiredMixin, View):
    """版本发布时间轴视图"""
    def get(self, request: HttpRequest) -> HttpResponse:
        changelogs = Changelog.objects.all()
        return render(request, 'netbox_changelog/changelog_releases.html', {
            'changelogs': changelogs,
        })

class ChangelogListView(generic.ObjectListView):
    queryset = Changelog.objects.all()
    table = ChangelogTable
    filterset = ChangelogFilterSet
    filterset_form = ChangelogFilterForm
    template_name = 'netbox_changelog/changelog_list.html'

class ChangelogBulkImportView(generic.BulkImportView):
    queryset = Changelog.objects.all()
    model = Changelog
    model_form = ChangelogImportForm
    table = ChangelogTable

@register_model_view(Changelog)
class ChangelogView(generic.ObjectView):
    queryset = Changelog.objects.all()
    template_name = 'netbox_changelog/changelog.html'

class ChangelogEditView(generic.ObjectEditView):
    queryset = Changelog.objects.all()
    form = ChangelogForm

class ChangelogDeleteView(generic.ObjectDeleteView):
    queryset = Changelog.objects.all()

class ChangelogBulkDeleteView(generic.BulkDeleteView):
    queryset = Changelog.objects.all()
    table = ChangelogTable

@register_model_view(Changelog, 'bulk_edit', path='edit', detail=False)
class ChangelogBulkEditView(generic.BulkEditView):
    queryset = Changelog.objects.all()
    filterset = ChangelogFilterSet
    table = ChangelogTable
    form = ChangelogBulkEditForm

    def get_required_permission(self) -> str:
        return 'netbox_changelog.change_changelog'
    
    def get_object(self, **kwargs: Any) -> None:
        return None
    
    def get_return_url(self, request: HttpRequest, obj: Model = None) -> str:
        return reverse('plugins:netbox_changelog:changelog_list')
