from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import Changelog

class ChangelogSerializer(NetBoxModelSerializer):
    class Meta:
        model = Changelog
        fields = (
            'id', 'url', 'display', 'date', 'version', 'category', 'title', 
            'description', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'date', 'version', 'category', 'title',
        )
