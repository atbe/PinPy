"""client script"""
import pypin
import os
from pprint import pprint

api = pypin.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])

# getting a pin using the experimental v3 of the api
pin = api.get_public_pin_v3('521713938070463188')
del pin._data['feedback_options']
pprint(pin.to_json())

# print API_CLIENT.create_board({'name': 'test3'})

# print API_CLIENT.create_pin({
#     'board': 'yvesfu/test3',
#     'note': 'a new pin',
#     'link': 'https://www.spartasales.com',
#     'image_url': 'http://img.over-blog-kiwi.com/0/86/68/47/20140304/ob_9b442c_baby-115a.jpg'
# })
