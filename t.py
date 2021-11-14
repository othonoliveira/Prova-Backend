import requests

url='https://www.hugedomains.com/checkout.cfm'

data={
    'userFirstName': 'kjnlbkjrG LKJBW',
    'userLastName': 'Kebwwwkbwn',
    'email': 'ty963828@gmail.com',
    'phoneCode': '55',
    'phone': '6841846184',
    'card': '5555666677778884',
    'firstLastName': 'Wlehquhil',
    'month': '12',
    'year': '2022',
    'code': '123',
    'address': '123',
    'address2': '123',
    'city': '123',
    'state': 'New Brunswick',
    'zip': '64164182',
    'countryID': '4',
    'freeWhoIsPrivacy': '1',
    'e': '1',
    'totalPrice': '2395.00',
    'loadTime': '{ts "2021-09-28 14:13:17"}',
    'jse': '42',
    'ddat': '{"device_session_id":"168322900824ed59b1cf6f182c1a4a03","fraud_merchant_id":"603590"}',
    'hasJS': '1'
}

response = requests.post(url, data=data).text

print(response)