keyid='rzp_test_6Va4Hd02kimvK7'
secret_key='BWwg7VKkb8eNj4iFUmhAuzEH'

import razorpay
client=razorpay.Client(auth=(keyid,secret_key))


data={
    'amount':100*100,
    'currency':'INR',
    'receipt':'Successful Transaction',
    'notes':{
        'name':'Manish',
        'PAyment_for':'GroceryItems'
    }
}

order=client.order.create(data=data)
order_id=(order['id'])
