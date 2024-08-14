from bs4 import BeautifulSoup
import lxml.etree
from my_libraries.prettyprint import treeprint

def find_deep_text(element, trigger):
    if element.name == 'div' and trigger in element.get('class', []):
        return element.text
    for child in element.find_all('div'):
        text = find_deep_text(child, trigger)
        if text:
            return text
    return None

def parse_tree_list(tree_list):
    name = find_deep_text(tree_list, "trigger")
    dicto = {name: {}}

    item_container = tree_list.find('div', class_='item-container')
    if item_container:
        selectable_item_container = item_container.find('div', 'selectable-item-container')
        selectable_item_container_elem = lxml.etree.fromstring(str(selectable_item_container), parser=lxml.etree.HTMLParser())
        selectable_item_container_xpath = selectable_item_container_elem.getroottree().getpath(selectable_item_container_elem)

        dropdown_icon = item_container.find('material-icon', class_='zippy')
        if dropdown_icon:
            dropdown_icon_elem = lxml.etree.fromstring(str(dropdown_icon), parser=lxml.etree.HTMLParser())
            dropdown_xpath = dropdown_icon_elem.getroottree().getpath(dropdown_icon_elem)
            dicto[name]["selectable_xpath"] = selectable_item_container_xpath
            dicto[name]["dropdown_xpath"] = dropdown_xpath

            subitems = tree_list.find('div', class_='subitems')
            if subitems:
                dicto[name]["children"] = {}
                for sub_tree_list in subitems.find_all('tree-list', recursive=False):
                    sub_dicto = parse_tree_list(sub_tree_list)
                    dicto[name]["children"].update(sub_dicto)
        else:
            dicto[name]["selectable_xpath"] = selectable_item_container_xpath

    return dicto

def main(html_path):
    with open(html_path, 'r') as file:
        html = file.read()
    treeprint(parse_tree_list(BeautifulSoup(html, 'html.parser')))

if __name__ == '__main__':
    main('the_second_small_one.txt')