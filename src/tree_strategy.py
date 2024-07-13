# tree_strategy.py

from strategy import DisplayStrategy

class TreeDisplayStrategy(DisplayStrategy):
    def display(self, component, indent='', is_last=True, icon_family=None, is_root=False):
        icon = icon_family.get_icon('inner') if icon_family else ''
        if is_root:
            new_indent = indent
        else:
            prefix = '└─' if is_last else '├─'
            print(f"{indent}{prefix} {icon}{component.key}")
            new_indent = indent + ('    ' if is_last else '│   ')

        iterator = component.create_iterator()
        while iterator.has_next():
            child = iterator.next()
            is_last_child = not iterator.has_next()
            child.display(strategy=self, indent=new_indent, is_last=is_last_child, icon_family=icon_family, is_root=False)
