# import json
# from loader import db
# from functions.callback_generator import callback_data_generator


# with open('mac.json', 'r') as file:
#     data = json.load(file)

# main_callback_data = 'mac'

# for item in data['children'][0]['children']:
#     if item['children'][1]['name'] is None:
#         continue
#     text = item['children'][1]['name']
#     own_callback_data = callback_data_generator(text=text.split(".")[0])
#     db.add_inner_categories(main_callback_data=main_callback_data, text=text, own_callback_data=own_callback_data)






























import json
from loader import db
from functions.callback_generator import callback_data_generator


with open('categories.json', 'r') as file:
    data = json.load(file)

# main_callback_data = callback_data_generator(data['children'][0]['children'][0]['name'])

for item in data['children'][0]['children'][0]['children']:
    if item['name'] is None:
        continue
    text = item['name']
    own_callback_data = callback_data_generator(item['name'])
    db.add_categories(text=text, callback_data=own_callback_data)
