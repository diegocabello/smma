from bs4 import BeautifulSoup
import lxml.etree as etree
from my_libraries.bigstringer import bigstringer

def print_dict(dictionary, indent=0):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print(" " * indent + f'"{key}": ' + "{")
            print_dict(value, indent + 4)
            print(" " * indent + "},")
        else:
            print(" " * indent + f'"{key}": "{value}",')

def find_deep_text(element, trigger):
    if element.name == 'div' and trigger in element.get('class', []):
        return element.text
    for child in element.find_all('div'):
        text = find_deep_text(child, trigger)
        if text:
            return text
    return None

def custom_prettify_html(html_str, indent_size=4):
    lines = html_str.split('\n')
    custom_indented_lines = []
    for line in lines:
        stripped_line = line.lstrip()
        leading_spaces = len(line) - len(stripped_line)
        indented_line = ' ' * (leading_spaces * indent_size) + stripped_line
        custom_indented_lines.append(indented_line)
    return '\n'.join(custom_indented_lines)

def parse_tree_list(name, tree_list, search_for_list, parent_xpath=''):

    dicto = {name: {}}
    print(f'\n{"=" * 20}{name}{(80 - len(name)) * "="}\n')
    tree_list_xpath = parent_xpath + '/' + BeautifulSoup(tree_list, 'html.parser').name 
    pretty_tree_root_elem = BeautifulSoup(str(tree_list), 'html.parser').prettify()
    print(custom_prettify_html(pretty_tree_root_elem))

    alto_dicto = {}

    for index, child in enumerate(direct_children = [child for child in tree_list.children if child.name is not None]):
        for query in search_for_list:
            if isinstance(query, str):
                if child.find(query, recursive=False):
                    alto_dicto[query] = parse_tree_list(query, child, search_for_list, parent_xpath)
            elif isinstance(query, tuple):
                if child.find(query[0], class_=query[1], recursive=False):
                    alto_dicto[query[1]] = parse_tree_list()


    item_container = tree_list.find('div', class_='item-container')
    if item_container:
        dicto[name]["selectable_xpath"] = tree_list_xpath + '/' + item_container.find('div', 'selectable-item-container').name 
        print(parent_xpath)
        print(tree_list_xpath + '/' + item_container.find('div', 'selectable-item-container').name )

        dropdown_icon = item_container.find('material-icon', class_='zippy')
        if dropdown_icon:
            dicto[name]["dropdown_xpath"] = tree_list_xpath + '/' 

    subitems_div = tree_list.find('div', class_='subitems')
    if subitems_div:
        dicto[name]["children"] = {}
        for index, sub_tree_list in enumerate(subitems_div.find_all('tree-list', recursive=False), start=1):
            sub_dicto = parse_tree_list(find_deep_text(sub_tree_list, "trigger"), sub_tree_list, f'/div[{index}]' + f'/tree-list[{index}]')
            dicto[name]["children"].update(sub_dicto)

    return dicto

def main(html_path):
    html = bigstringer(html_path)
    found_the_tree = BeautifulSoup(html, 'html.parser').find('tree-list')
    ttbp = parse_tree_list('root', found_the_tree)
    print("{")
    print_dict(ttbp, 4)
    print("}")

if __name__ == '__main__':
    main('the_second_small_one.txt')

the_list = [('div', 'subitems'), ('div', 'selectable-item-container'), ('div', 'item-container'), ('material-icon', 'zippy'), 'tree-list']