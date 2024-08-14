from bs4 import BeautifulSoup
import lxml.etree as etree
from my_libraries.prettyprint import treeprint

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

def parse_tree_list(tree_list, parent_xpath=''):

    if parent_xpath != '':
        name = find_deep_text(tree_list, "trigger") if find_deep_text(tree_list, "trigger") else 'root'
    else:
        name='root'
    dicto = {name: {}}
    print(f'\n{"=" * 20}{name}{(80 - len(name)) * "="}\n')
    print(parent_xpath)
    print('\n')
        
    tree_list_xpath = parent_xpath + '/' + tree_list.name
    #pretty_tree_root_elem = BeautifulSoup(str(tree_list), 'html.parser').prettify()
    #print(custom_prettify_html(pretty_tree_root_elem))

    item_container = tree_list.find('div', class_='item-container')
    print(len(item_container))
    if item_container:
        selectable_item_container = item_container.find('div', 'selectable-item-container')
        selectable_item_container_xpath = tree_list_xpath + '/' + selectable_item_container.name 
        print(selectable_item_container_xpath)
        dicto[name]["selectable_xpath"] = selectable_item_container_xpath

        dropdown_icon = item_container.find('material-icon', class_='zippy')
        if dropdown_icon:
            dropdown_icon_xpath = tree_list_xpath + '/' + dropdown_icon.name 
            dicto[name]["dropdown_xpath"] = f"{dropdown_icon_xpath}"

    subitems_div = tree_list.find('div', class_='subitems')
    if subitems_div:
        dicto[name]["children"] = {}
        for index, sub_tree_list in enumerate(subitems_div.find_all('tree-list', recursive=False)[:5], start=1):
            sub_dicto = parse_tree_list(sub_tree_list, tree_list_xpath + f'/tree-list[{index}]')
            dicto[name]["children"].update(sub_dicto)

    return dicto

def main(html_path):
    with open(html_path, 'r') as file:
        html = file.read()
    found_the_tree = BeautifulSoup(html, 'html.parser').find('tree-list')
    treeprint(parse_tree_list(found_the_tree))

if __name__ == '__main__':
    main('the_second_small_one.txt')