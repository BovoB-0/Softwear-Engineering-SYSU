class IconFamily:
    def __init__(self, icons):
        self.icons = icons

    def get_icon(self, node_type):
        return self.icons.get(node_type, '')


class IconFactory:
    def __init__(self, config):
        self.config = config

    def get_icon_family(self, name):
        icons = self.config.get(name, {})
        return IconFamily(icons)
