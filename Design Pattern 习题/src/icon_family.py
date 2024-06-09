import json


class IconFamily:
    def get_icon(self, node_type):
        pass


class DefaultIconFamily(IconFamily):
    def get_icon(self, node_type):
        if node_type == 'inner':
            return '├─'
        elif node_type == 'leaf':
            return '└─'
        return ''


class PokerFaceIconFamily(IconFamily):
    def get_icon(self, node_type):
        if node_type == 'inner':
            return '♢'
        elif node_type == 'leaf':
            return '♤'
        return ''


class EmojiIconFamily(IconFamily):  # 新增的图标族
    def __init__(self):
        super().__init__({"inner": "😊", "leaf": "🍎"})


class ConfigurableIconFamily(IconFamily):
    def __init__(self, config):
        self.config = config

    def get_icon(self, node_type):
        return self.config.get(node_type, '')


class IconFamilyFactory:
    @staticmethod
    def load_icon_config(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)

    @staticmethod
    def create_icon_family(family_type, config_file='icon_config.json'):
        config = IconFamilyFactory.load_icon_config(config_file)
        if family_type in config:
            return ConfigurableIconFamily(config[family_type])
        raise ValueError(f"Unknown icon family type: {family_type}")
