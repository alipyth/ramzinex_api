import requests


API = 'کلید API را اینجا قرار دهید'


body = {
    'secret' : 'کلید خصوصی',
    'api_key' : API

}

gettoken = requests.post('https://ramzinex.com/exchange/api/v1.0/exchange/auth/api_key/getToken' , data=body)

bearer = gettoken.json()['data']['token']
print(bearer)

#سفارش بازار

headers= {
    'Authorization2' : f'bearer {bearer}',
    'x-api-key' : API
}

payload = {
    'pair_id' : 5,
    'amount' : 0.1,
    'type' : 'buy' #sell
}
order = requests.post('https://ramzinex.com/exchange/api/v1.0/exchange/users/me/orders/market' , json=payload, headers=headers)
print(order.json())


#کیف پول
wallet = requests.get('https://ramzinex.com/exchange/api/v1.0/exchange/users/me/funds/available/currency/4' , headers=headers)
print(wallet.text)


#کنسل کردن سفارش
ordernumber = 4324323423
cancel = requests.post(f'https://ramzinex.com/exchange/api/v1.0/exchange/users/me/orders/{ordernumber}/cancel' , headers=headers)
print(cancel.json())



