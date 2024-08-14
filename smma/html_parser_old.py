from bs4 import BeautifulSoup
from bs4.element import Comment
import lxml.etree as etree
from my_libraries.prettyprint import treeprint
from my_libraries.bigstringer import bigstringer

prepath = '/html/body/div[3]/div[13]/div/div[2]/div/div[3]/lazy-plugin/div/dynamic-component/campaign-audiences/material-expansionpanel/div/div[2]/div/div[1]/div/div/div/div[2]/audience-picker/picker/div/div/div/div/dynamic-component/picker-section/div/div[1]/div[2]/div/div/subcategory-tree/div/div/div/subcategory-renderer/div[2]/div/tree-list'

def find_deep_text(element, trigger):
    if element.name == 'div' and trigger in element.get('class', []):
        return element.text
    for child in element.find_all('div'):
        text = find_deep_text(child, trigger)
        if text:
            return text
    return None

def print_dict(dictionary, indent=0):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print(" " * indent + f'"{key}": ' + "{")
            print_dict(value, indent + 4)
            print(" " * indent + "},")
        else:
            print(" " * indent + f'"{key}": "{value}",')

def custom_prettify_html(html_str, indent_size=4):
    lines = html_str.split('\n')
    custom_indented_lines = []
    for line in lines:
        stripped_line = line.lstrip()
        leading_spaces = len(line) - len(stripped_line)
        indented_line = ' ' * (leading_spaces * indent_size) + stripped_line
        custom_indented_lines.append(indented_line)
    return '\n'.join(custom_indented_lines)

def parse_element(input_element, parent_xpath):

    if parent_xpath != prepath:
        name = find_deep_text(input_element, "trigger") if find_deep_text(input_element, "trigger") else 'root'
    else:
        name='root'
    dicto = {name: {}}

    for item_index, item in enumerate([div for div in input_element.children if type(div).__name__ != 'Comment'], start=1):

        if 'item-container' in item.get('class', []):
            selectable_item_container_xpath = parent_xpath + f'/div[{str(item_index)}]/div'
            print(selectable_item_container_xpath)
            dicto[name]["selectable_xpath"] = selectable_item_container_xpath

            dropdown_icon = item.find('material-icon', class_='zippy')
            if dropdown_icon:
                dicto[name]["dropdown_xpath"] = parent_xpath + '/' + dropdown_icon.name 

        if 'subitems' in item.get('class', []):
            dicto[name]["children"] = {}
            for index, sub_input_element in enumerate(item.find_all('tree-list', recursive=False)[:5], start=1):
                sub_dicto = parse_element(sub_input_element, parent_xpath + f'/div[{str(item_index)}]/tree-list[{index}]')
                dicto[name]["children"].update(sub_dicto)

    return dicto

def main(html_path):
    html = bigstringer(html_path)
    found_the_tree = BeautifulSoup(html, 'html.parser')
    ttbp = parse_element(found_the_tree, prepath)
    print("{")
    print_dict(ttbp, 4)
    print("}")

if __name__ == '__main__':
    main('the_third_one.txt')
