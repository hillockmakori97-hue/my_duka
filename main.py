from flask import Flask,render_template
from database import view_products



app= Flask(__name__)
@app.route('/')
def home():
    number=100
    return render_template('index.html',value = number)

@app.route('/products')
def products():
   products_data=view_products(products)
   return render_template('products.html',products_data=products_data)


@app.route('/sales')
def sales():
    return render_template('sales.html')


@app.route('/login')
def login():
    return render_template('login.html') 


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')


@app.route('/index')
def index():
    return render_template('index.html')

app.run()