from django.urls import include, path
from utilities.urls import get_model_urls
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = [
    path('logs/', views.ChangelogListView.as_view(), name='changelog_list'),
    path('logs/add/', views.ChangelogEditView.as_view(), name='changelog_add'),
    path('logs/import/', views.ChangelogBulkImportView.as_view(), name='changelog_bulk_import'),
    path('logs/edit/', views.ChangelogBulkEditView.as_view(), name='changelog_bulk_edit'),
    path('logs/bulk-delete/', views.ChangelogBulkDeleteView.as_view(), name='changelog_bulk_delete'),
    path('logs/<int:pk>/', include(get_model_urls('netbox_changelog', 'changelog'))),
    path('logs/<int:pk>/edit/', views.ChangelogEditView.as_view(), name='changelog_edit'),
    path('logs/<int:pk>/delete/', views.ChangelogDeleteView.as_view(), name='changelog_delete'),
    path('logs/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='changelog_changelog', kwargs={'model': models.Changelog}),
]
