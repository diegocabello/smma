from bs4 import BeautifulSoup, Tag
import lxml.etree
from my_libraries.prettyprint import treeprint

def find_deep_text(element, trigger):
    if isinstance(element, tuple):
        element = element[0]
    if isinstance(element, Tag):
        if element.name == 'div' and trigger in element.get('class', []):
            return element.text
        for child in element.find_all('div'):
            text = find_deep_text(child, trigger)
            if text:
                return text
    return None

def parse_tree_list(name, tree_list):
        
    dicto={name: {}}

    subitems_div_list = tree_list.find_all('tree-list', recursive=False)
    if subitems_div_list:
        for sub_tree_list in subitems_div_list:
            name = find_deep_text(sub_tree_list, "trigger")
            sub_dicto = parse_tree_list(sub_tree_list)
            dicto[name] = sub_dicto

    return dicto

def main(html_path):
    with open(html_path, 'r') as file:
        html = file.read()
    found_the_tree = BeautifulSoup(html, 'html.parser').find('tree-list', recursive=False)
    treeprint(parse_tree_list(name='root', tree_list=found_the_tree))

if __name__ == '__main__':
    main('the_second_small_one.txt')


            # tree_list_elem = lxml.etree.fromstring(str(tree_list), parser=lxml.etree.HTMLParser())
            # tree_list_xpath = parent_xpath + '/' + tree_list_elem.tag + ''.join([f"[@{attr}='{val}']" for attr, val in tree_list_elem.attrib.items()])

            # item_container = tree_list.find('div', class_='item-container')
            # if item_container:
            #     selectable_item_container = item_container.find('div', 'selectable-item-container')
            #     selectable_item_container_xpath = tree_list_xpath + '/' + selectable_item_container.name + ''.join([f"[@class='{c}']" for c in selectable_item_container.get('class', [])])
            #     dicto[name]["selectable_xpath"] = f"{selectable_item_container_xpath}"

            #     dropdown_icon = item_container.find('material-icon', class_='zippy')
            #     if dropdown_icon:
            #         dropdown_icon_xpath = tree_list_xpath + '/' + dropdown_icon.name + ''.join([f"[@class='{c}']" for c in dropdown_icon.get('class', [])])
            #         dicto[name]["dropdown_xpath"] = f"{dropdown_icon_xpath}"

            # subitems_div = tree_list.find_all('div', class_='subitems', recursive=False)
            # if subitems_div:
            #     dicto[name]["children"] = {}
            #     for index, sub_tree_list in enumerate(subitems_div.find_all('tree-list', recursive=False), start=1):
            #         sub_dicto = parse_tree_list(sub_tree_list, tree_list_xpath + f'/tree-list[{index}]')
            #         dicto[name]["children"].update(sub_dicto)

