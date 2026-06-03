from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

menu = PluginMenu(
    label='更新日志',
    groups=(
        ('更新日志', (
            PluginMenuItem(
                link='plugins:netbox_changelog:changelog_list',
                link_text='更新日志',
                permissions=['netbox_changelog.view_changelog'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_changelog:changelog_add',
                        title='添加',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_changelog.add_changelog'],
                    ),
                )
            ),
        )),
    ),
    icon_class='mdi mdi-history',
)
