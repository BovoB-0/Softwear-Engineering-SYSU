class Style:
    def display(self, json_obj, icon_family):
        pass


class TreeStyle(Style):
    def display(self, json_obj, icon_family):
        json_obj.display(0, icon_family)


class RectangleStyle(Style):
    def display(self, json_obj, icon_family):
        json_obj.display(0, icon_family)


class IndentedStyle(Style):
    def display(self, json_obj, icon_family):
        json_obj.display(0, icon_family, indented=True)


class StyleFactory:
    @staticmethod
    def create_style(style_type):
        if style_type == 'tree':
            return TreeStyle()
        elif style_type == 'rectangle':
            return RectangleStyle()
        elif style_type == 'indented':
            return IndentedStyle()
        raise ValueError(f"Unknown style type: {style_type}")
