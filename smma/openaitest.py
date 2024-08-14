from openai import OpenAI
from interests_and_habits_dict import dicto, simple_dicto
import ast

client = OpenAI(
  organization = '',
  project = '',
  api_key = "",
)

print('connected...')

def product(product: str):
    return client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        #{"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": f"{simple_dicto} \n \
        From this dictionary, which is used for search engine optimization, which categories would best fit the product '{product}'? \
        Be not so strict on product categories; you can give it categories where it would only kind of fit in. \n \
        Return the answer ONLY as a Python dictionary, no text in the front or the back, and in one line as a Python dictionary, no new lines or indents. \
        If you pick something nested in something, make sure that it has its parent elements all the way up. \
        Return it in the format like {{\"root\":{{\"children\":{{\"Banking & Finance\":{{\"children\":{{\"Avid Investors\"}}}}}}}}}}\
        make sure to include the first root and children, every time an element is embedded inside another element, include it inside the children element. that is very strict"}
        ]
    ).choices[0].message.content

def recursor(inputer_dict, reference_dict=dicto):
    if isinstance(inputer_dict, str):
        inputer_dict = ast.literal_eval(inputer_dict) 
    return_list = []
    for key, value in inputer_dict.items():
        if key in reference_dict:
            pass_reference_dict = reference_dict[key]
            if 'selectable_xpath' in pass_reference_dict:
                return_list.append({"selectable": pass_reference_dict['selectable_xpath']})
            if 'dropdown_xpath' in pass_reference_dict:
                return_list.append({"dropdown": pass_reference_dict['dropdown_xpath']})
            if 'children' in pass_reference_dict and value:
                return_list.extend(recursor(value['children'], pass_reference_dict['children']))
    return return_list

def main(query='sewed blanked'):
    ff = product(query)
    print(ff)
    print('\n\n')
    for x in recursor(ff):
        print(x)

if __name__ == '__main__':
    main()
