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

def parse_tree_list(name, tree_list, parent_xpath=''):

    dicto = {name: {}}

    #tree_list_elem = etree.fromstring(str(tree_list), parser=etree.HTMLParser())
    tree_list_xpath = parent_xpath + '/' + BeautifulSoup(tree_list, 'html.parser').name 

    item_container = tree_list.find('div', class_='item-container')
    if item_container:
        dicto[name]["selectable_xpath"] = tree_list_xpath + '/' + item_container.find('div', 'selectable-item-container').name 

        dropdown_icon = item_container.find('material-icon', class_='zippy')
        if dropdown_icon:
            dicto[name]["dropdown_xpath"] = tree_list_xpath + '/' 

    subitems_div = tree_list.find('div', class_='subitems')
    if subitems_div:
        dicto[name]["children"] = {}
        for index, sub_tree_list in enumerate(subitems_div.find_all('tree-list', recursive=False), start=1):
            #what it was: sub_dicto = parse_tree_list(find_deep_text(sub_tree_list, "trigger"), sub_tree_list, tree_list_xpath + f'/tree-list[{index}]')
            sub_dicto = parse_tree_list(find_deep_text(sub_tree_list, "trigger"), sub_tree_list, f'/div[{index}]' + f'/tree-list[{index}]')
            dicto[name]["children"].update(sub_dicto)

    return dicto

def main(html_path):
    #with open(html_path, 'r') as file:
    #    html = file.read()
    html = bigstringer(html_path)
    found_the_tree = BeautifulSoup(html, 'html.parser').find('tree-list')
    ttbp = parse_tree_list('root', found_the_tree)
    print("{")
    print_dict(ttbp, 4)
    print("}")

if __name__ == '__main__':
    main('the_second_small_one.txt')