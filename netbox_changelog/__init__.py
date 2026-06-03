from netbox.plugins import PluginConfig

class NetBoxChangelogConfig(PluginConfig):
    name: str = 'netbox_changelog'
    verbose_name: str = '更新日志'
    description: str = '用于记录系统变更、升级和配置修改的日志插件'
    version: str = '0.1.0'
    base_url: str = 'changelog'
    author: str = 'Changelog Team'
    author_email: str = 'changelog@example.com'
    required_settings: list[str] = []
    default_settings: dict = {}
    
    # Netbox 4.x compatibility
    min_version: str = '4.0'
    max_version: str = '4.99'
    
    def ready(self) -> None:
        super().ready()
        
        # Register API URLs
        from . import api

config = NetBoxChangelogConfig
