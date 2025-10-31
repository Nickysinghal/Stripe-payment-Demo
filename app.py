from flask import Flask, render_template,abort, redirect,request
import stripe
import os
from dotenv import load_dotenv #as flask itself doesn’t automatically read .env
load_dotenv() #load .env file

app = Flask(__name__)
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

products = {
    'megatutorial':{
        'name':'The Flask Mega Tutorial',
        'price':50
    },
    
    'support':{
        'name' : 'Python 1:1 Support',
        'price' : 20000,
        'per' : 'hour',
        'adjustable_quantity':{
            'enabled':True,
            'minimum':1,
            'maximum':4
        },
    },
}

@app.route('/')
def index():
    return render_template("index.html",products= products)

@app.route('/order/<product_id>',methods=['POST'])
def order(product_id):
    if(product_id not in products):
        abort(404)
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data':{
                    'product_data':{
                        'name':products[product_id]['name'],
                    },
                    'unit_amount':products[product_id]['price'],
                    'currency':'usd',
                },
                'quantity':1,
                'adjustable_quantity':products[product_id].get(
                    'adjustable_quantity',{'enabled':False}
                ),
            },
        ],
        
        payment_method_types=['card'],
        mode='payment',
        success_url=request.host_url+'order/success',
        cancel_url=request.host_url+'order/cancel',
        
    )    
    return redirect(checkout_session.url)

@app.route('/order/success')
def success():
    return render_template("success.html")

@app.route('/order/cancel')
def cancel():
    return render_template("cancel.html")

if __name__ == "__main__":
    app.run(debug=True)