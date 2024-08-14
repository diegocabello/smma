from bs4 import BeautifulSoup
import lxml.etree

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
    
    tree_list_elem = lxml.etree.fromstring(str(tree_list), parser=lxml.etree.HTMLParser())
    tree_list_xpath = tree_list_elem.getroottree().getpath(tree_list_elem)
    
    if tree_list.find('div', class_='item-container'):
        item_container = tree_list.find('div', class_='item-container')
        selectable_item_container_elem = item_container.find('div', class_='selectable-item-container')
        selectable_item_container_xpath = tree_list_xpath + '/' + selectable_item_container_elem.name + ''.join([f"[@class='{c}']" for c in selectable_item_container_elem.get('class', [])])
        
        if tree_list.find('material-icon') and tree_list.find('material-icon').find('i'):
            arr = tree_list.find('material-icon').find('i')
            arr_elem = lxml.etree.fromstring(str(arr), parser=lxml.etree.HTMLParser())
            arr_xpath = tree_list_xpath + '/material-icon/i'
            dicto[name] = {"selectable_xpath": selectable_item_container_xpath, "dropdown_xpath": arr_xpath}
        else:
            dicto[name] = {"selectable_xpath": selectable_item_container_xpath}
    
    if tree_list.find('div', class_='subitems'):
        dicto[name].setdefault("children", {})
        for sub_tree_list in tree_list.find('div', class_='subitems').find_all('tree-list'):
            sub_name = find_deep_text(sub_tree_list, "trigger")
            dicto[name]["children"][sub_name] = parse_tree_list(sub_tree_list)[sub_name]
    
    return dicto

def main(html):
    soup = BeautifulSoup(html, 'html.parser')
    print(parse_tree_list(soup))

# Example usage
html = '''
<tree-list class="tree-list _nghost-awn-CM_EDITING-224 _ngcontent-awn-CM_EDITING-223"><!----><!----><!----><div class="subitems _ngcontent-awn-CM_EDITING-224" id="a31377049-5A0D-45B9-95E2-F5EDA7E274DD--139" role="group"><!----><tree-list class="_ngcontent-awn-CM_EDITING-224 _nghost-awn-CM_EDITING-224"><!----><!----><div class="item-container _ngcontent-awn-CM_EDITING-224 pointer checkbox-padding" role="treeitem" aria-expanded="true" aria-selected="false" aria-disabled="false" tabindex="0" aria-owns="a31377049-5A0D-45B9-95E2-F5EDA7E274DD--140"><div class="selectable-item-container _ngcontent-awn-CM_EDITING-224"><!----><material-checkbox class="themeable _nghost-awn-CM_EDITING-76 _ngcontent-awn-CM_EDITING-224" tabindex="-1" aria-checked="false" aria-labelledby="a014BF4AF-668A-4D26-BE97-88EC3C35B23C--284" role="checkbox" aria-disabled="false"><div aria-hidden="true" class="icon-container _ngcontent-awn-CM_EDITING-76"><material-icon class="icon _nghost-awn-CM_EDITING-18 _ngcontent-awn-CM_EDITING-76"><i class="material-icon-i material-icons-extended _ngcontent-awn-CM_EDITING-18" role="img" aria-hidden="true">check_box_outline_blank</i></material-icon><!----><material-ripple aria-hidden="true" class="ripple _ngcontent-awn-CM_EDITING-76"></material-ripple><div class="focus-ring _ngcontent-awn-CM_EDITING-76"></div></div><div class="content _ngcontent-awn-CM_EDITING-76"> </div></material-checkbox><!----><div autoid="" class="item _ngcontent-awn-CM_EDITING-224" id="a014BF4AF-668A-4D26-BE97-88EC3C35B23C--284"><div class="_ngcontent-awn-CM_EDITING-224"></div><audience-renderer class="_nghost-awn-CM_EDITING-225"><div class="criterion _ngcontent-awn-CM_EDITING-225"><span class="criteria-name _ngcontent-awn-CM_EDITING-225"><!----> <!----><!----><audience-info-trigger class="_ngcontent-awn-CM_EDITING-225 _nghost-awn-CM_EDITING-119"><div class="trigger _ngcontent-awn-CM_EDITING-119" keyboardonlyfocusindicator="" popupsource="" role="button" tabindex="0">Banking &amp; Finance</div><!----><!----><!----></audience-info-trigger><custom-audience-approval-icon class="_ngcontent-awn-CM_EDITING-225 _nghost-awn-CM_EDITING-120"><!----></custom-audience-approval-icon><!----></span> <!----><!----></div></audience-renderer><!----><!----></div></div><!----><material-icon buttondecorator="" class="zippy _nghost-awn-CM_EDITING-18 _ngcontent-awn-CM_EDITING-224" aria-label="Collapse items" role="button" aria-disabled="false"><i class="material-icon-i material-icons-extended _ngcontent-awn-CM_EDITING-18" role="img" aria-hidden="true">expand_less</i></material-icon></div><!----><div class="subitems _ngcontent-awn-CM_EDITING-224 children" id="a31377049-5A0D-45B9-95E2-F5EDA7E274DD--140" role="group"><!----><tree-list class="_ngcontent-awn-CM_EDITING-224 _nghost-awn-CM_EDITING-224"><!----><!----><div class="item-container _ngcontent-awn-CM_EDITING-224 pointer checkbox-padding" role="treeitem" aria-selected="false" aria-disabled="false"><div class="selectable-item-container _ngcontent-awn-CM_EDITING-224"><!----><material-checkbox class="themeable _nghost-awn-CM_EDITING-76 _ngcontent-awn-CM_EDITING-224" tabindex="-1" aria-checked="false" aria-labelledby="a014BF4AF-668A-4D26-BE97-88EC3C35B23C--298" role="checkbox" aria-disabled="false"><div aria-hidden="true" class="icon-container _ngcontent-awn-CM_EDITING-76"><material-icon class="icon _nghost-awn-CM_EDITING-18 _ngcontent-awn-CM_EDITING-76"><i class="material-icon-i material-icons-extended _ngcontent-awn-CM_EDITING-18" role="img" aria-hidden="true">check_box_outline_blank</i></material-icon><!----><material-ripple aria-hidden="true" class="ripple _ngcontent-awn-CM_EDITING-76"></material-ripple><div class="focus-ring _ngcontent-awn-CM_EDITING-76"></div></div><div class="content _ngcontent-awn-CM_EDITING-76"> </div></material-checkbox><!----><div autoid="" class="item _ngcontent-awn-CM_EDITING-224 no-zippy-padding" id="a014BF4AF-668A-4D26-BE97-88EC3C35B23C--298"><div class="_ngcontent-awn-CM_EDITING-224"></div><audience-renderer class="_nghost-awn-CM_EDITING-225"><div class="criterion _ngcontent-awn-CM_EDITING-225"><span class="criteria-name _ngcontent-awn-CM_EDITING-225"><!----> <!----><!----><audience-info-trigger class="_ngcontent-awn-CM_EDITING-225 _nghost-awn-CM_EDITING-119"><div class="trigger _ngcontent-awn-CM_EDITING-119" keyboardonlyfocusindicator="" popupsource="" role="button" tabindex="0" aria-haspopup="true">Avid Investors</div><!----><material-popup enforcespaceconstraints="" role="tooltip" tracklayoutchanges="" class="_ngcontent-awn-CM_EDITING-119 _nghost-awn-CM_EDITING-58 popup-transform" aria-label="Audience info for Avid Investors" pane-id="CM_EDITING--53"><!---->
</material-popup><!----><!----></audience-info-trigger><custom-audience-approval-icon class="_ngcontent-awn-CM_EDITING-225 _nghost-awn-CM_EDITING-120"><!----></custom-audience-approval-icon><!----></span> <!----><!----></div></audience-renderer><!----><!----></div></div><!----></div><!----><!----><!----></tree-list><tree-list class="_ngcontent-awn-CM_EDITING-224 _nghost-awn-CM_EDITING-224"><!----><!----><div class="item-container _ngcontent-awn-CM_EDITING-224 pointer checkbox-padding" role="treeitem" aria-selected="false" aria-disabled="false"><div class="selectable-item-container _ngcontent-awn-CM_EDITING-224"><!----><material-checkbox class="themeable _nghost-awn-CM_EDITING-76 _ngcontent-awn-CM_EDITING-224" tabindex="-1" aria-checked="false" aria-labelledby="a014BF4AF-668A-4D26-BE97-88EC3C35B23C--299" role="checkbox" aria-disabled="false"><div aria-hidden="true" class="icon-container _ngcontent-awn-CM_EDITING-76"><material-icon class="icon _nghost-awn-CM_EDITING-18 _ngcontent-awn-CM_EDITING-76"><i class="material-icon-i material-icons-extended _ngcontent-awn-CM_EDITING-18" role="img" aria-hidden="true">check_box_outline_blank</i></material-icon><!----><material-ripple aria-hidden="true" class="ripple _ngcontent-awn-CM_EDITING-76"></material-ripple><div class="focus-ring _ngcontent-awn-CM_EDITING-76"></div></div><div class="content _ngcontent-awn-CM_EDITING-76"> </div></material-checkbox><!----><div autoid="" class="item _ngcontent-awn-CM_EDITING-224 no-zippy-padding" id="a014BF4AF-668A-4D26-BE97-88EC3C35B23C--299"><div class="_ngcontent-awn-CM_EDITING-224"></div><audience-renderer class="_nghost-awn-CM_EDITING-225"><div class="criterion _ngcontent-awn-CM_EDITING-225"><span class="criteria-name _ngcontent-awn-CM_EDITING-225"><!----> <!----><!----><audience-info-trigger class="_ngcontent-awn-CM_EDITING-225 _nghost-awn-CM_EDITING-119"><div class="trigger _ngcontent-awn-CM_EDITING-119" keyboardonlyfocusindicator="" popupsource="" role="button" tabindex="0">Banks Online</div><!----><!----><!----></audience-info-trigger><custom-audience-approval-icon class="_ngcontent-awn-CM_EDITING-225 _nghost-awn-CM_EDITING-120"><!----></custom-audience-approval-icon><!----></span> <!----><!----></div></audience-renderer><!----><!----></div></div><!----></div><!----><!----><!----></tree-list></div><!----><!----><div class="divider lower _ngcontent-awn-CM_EDITING-224"></div></tree-list></div><!----><!----></tree-list>
'''

main(html)