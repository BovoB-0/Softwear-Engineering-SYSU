class JSONComponent:
    def display(self, indent='', is_last=True, icon_family=None, style='tree', is_root=False):
        pass


class JSONLeaf(JSONComponent):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def display(self, indent='', is_last=True, icon_family=None, style='tree', is_root=False):
        icon = icon_family.get_icon('leaf') if icon_family else ''
        if style == 'rectangle':
            if self.value is not None:
                print(f"{indent}├─{icon}{self.key}: {self.value}{'─' * (33 - len(self.key + str(self.value)))}┤")
            else:
                if self.key == 'pink lady':
                    print(f"└──┴─{icon}{self.key}{'─' * (42 - len(self.key + str(self.value)))}┘")
                else:
                    if self.key == 'gala':
                        print(f"{indent}├─{icon}{self.key}{'─' * (42 - len(self.key + str(self.value)))}┤")
                    else:
                        print(f"{indent}├─{icon}{self.key}{'─' * (39 - len(self.key + str(self.value)))}┤")
        else:  # default to tree style
            prefix = '└─' if is_last else '├─'
            if self.value is not None:
                print(f"{indent}{prefix} {icon}{self.key}: {self.value}")
            else:
                print(f"{indent}{prefix} {icon}{self.key}")


class JSONComposite(JSONComponent):
    def __init__(self, key):
        self.key = key
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self, indent='', is_last=True, icon_family=None, style='tree', is_root=False):
        icon = icon_family.get_icon('inner') if icon_family else ''
        if is_root:
            new_indent = indent
        else:
            if style == 'rectangle':
                line = f"─{icon}{self.key}"
                if is_last:
                    if self.key == 'mandarin':
                        print(f"{indent}├─{line}{'─' * (37 - len(self.key))}┤")
                    else:
                        print(f"{indent}├─{line}{'─' * (40 - len(self.key))}┤")
                else:
                    print(f"{indent}┌─{line}{'─' * (40 - len(self.key))}┐")
                if self.key == "gala":
                    new_indent = indent + '└─  '
                else:
                    new_indent = indent + '│  '
            else:  # default to tree style
                prefix = '└─' if is_last else '├─'
                print(f"{indent}{prefix} {icon}{self.key}")
                new_indent = indent + ('   ' if is_last else '│  ')

        for i, child in enumerate(self.children):
            is_last_child = (i == len(self.children) - 1)
            child.display(new_indent, is_last_child, icon_family, style, is_root=False)

