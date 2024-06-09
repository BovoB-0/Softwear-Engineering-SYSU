import json
import sys
from factories import JSONTreeFactory, JSONIndentedFactory, JSONRectangleFactory
from icon_factory import IconFactory


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Funny JSON Explorer")
    parser.add_argument('-f', '--file', required=True, help='JSON file to explore')
    parser.add_argument('-s', '--style', required=True, help='Display style: tree, indented, rectangle')
    parser.add_argument('-i', '--icon', required=True, help='Icon family: default, pokerface, star')
    parser.add_argument('-c', '--config', required=True, help='Icon config file')
    args = parser.parse_args()

    with open(args.file) as json_file:
        data = json.load(json_file)

    with open(args.config) as config_file:
        icon_config = json.load(config_file)

    if args.style == 'tree':
        factory = JSONTreeFactory()
    elif args.style == 'indented':
        factory = JSONIndentedFactory()
    elif args.style == 'rectangle':
        factory = JSONRectangleFactory()
    else:
        print("Invalid style")
        sys.exit(1)

    icon_factory = IconFactory(icon_config)
    icon_family = icon_factory.get_icon_family(args.icon)

    explorer = factory.create(data)
    explorer.display(icon_family=icon_family, style=args.style, is_root=True)


if __name__ == "__main__":
    main()
