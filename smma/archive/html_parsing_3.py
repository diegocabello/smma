from bs4 import BeautifulSoup
import lxml.etree
from my_libraries.prettyprint import treeprint

def find_deep_text(element, trigger):
    if element.name == 'div' and trigger in element.get('class'):
        return element.text
    for child in element.find_all('div'):
        text = find_deep_text(child, trigger)
        if text:
            return text
    return None

def generate_xpath(element):
    elem = lxml.etree.fromstring(str(element), parser=lxml.etree.HTMLParser())
    xpath = elem.getroottree().getpath(elem)
    return xpath

def parse_tree_list(tree_list):
    name = find_deep_text(tree_list, "trigger")
    dicto = {name: {}}

    if tree_list.find('div', class_='item-container'):
        item_container = tree_list.find('div', class_='item-container')
        selectable_item_container_elem = item_container.find('div', 'selectable-item-container')
        selectable_item_container_xpath = generate_xpath(selectable_item_container_elem)
        dicto[name]["selectable_xpath"] = selectable_item_container_xpath

        if tree_list.find('material-icon') and tree_list.find('material-icon').find('i', class_='material-icon-i'):
            arr = tree_list.find('material-icon').find('i', class_='material-icon-i')
            arr_xpath = generate_xpath(arr)
            dicto[name]["dropdown_xpath"] = arr_xpath

    if tree_list.find('div', class_='subitems'):
        dicto[name].setdefault("children", {})
        for sub_tree_list in tree_list.find('div', class_='subitems').find_all('tree-list'):
            sub_name = find_deep_text(sub_tree_list, "trigger")
            sub_dict = parse_tree_list(sub_tree_list)[sub_name]
            dicto[name]["children"][sub_name] = {"selectable_xpath": sub_dict["selectable_xpath"]}

    return dicto

def main(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    treeprint(parse_tree_list(soup))

if __name__ == '__main__':
    with open('the_second_small_one.txt', 'r') as file:
        html = file.read()
    main(html)