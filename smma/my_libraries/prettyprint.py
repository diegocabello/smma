from rich.tree import Tree
from rich import print as rprint
from rich.console import Console

def build_tree(node, data):
    if isinstance(data, dict):
        for key, value in data.items():
            branch = node.add(f"{key}:")
            build_tree(branch, value)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            branch = node.add(f"Item {i + 1}")
            build_tree(branch, item)
    else:
        node.add(f"{data}")


def treeprint(data):
    tree = Tree("Root")
    build_tree(tree, data)
    Console().print(tree)