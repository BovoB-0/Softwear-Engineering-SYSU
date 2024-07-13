# rectangle_strategy.py

from strategy import DisplayStrategy


class RectangleDisplayStrategy(DisplayStrategy):
    def display(self, component, indent='', is_last=True, icon_family=None, is_root=False):
        icon = icon_family.get_icon('inner') if icon_family else ''
        line = f"├─{icon}{component.key}"
        if is_last:
            print(f"{indent}└─{line}{'─' * (35 - len(component.key))}┘")
        else:
            print(f"{indent}┌─{line}{'─' * (35 - len(component.key))}┤")

        new_indent = indent + '│  '
        iterator = component.create_iterator()
        while iterator.has_next():
            child = iterator.next()
            is_last_child = not iterator.has_next()
            child.display(strategy=self, indent=new_indent, is_last=is_last_child, icon_family=icon_family,
                          is_root=False)

        if is_last:
            print(f"{indent}└{'─' * 38}┘")
        else:
            print(f"{indent}├{'─' * 38}┤")
