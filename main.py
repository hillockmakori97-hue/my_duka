from flask import Flask,render_template,request,redirect,url_for,flash
from database import view_table,insert_products,insert_sales,insert_stock,check_remaining_stock,check_user_exists,create_user
from flask_bcrypt import Bcrypt
import os

app= Flask(__name__)
# bcrypt instance with flask app
bcrypt=Bcrypt(app)

app.secret_key=os.urandom(24)
@app.route('/')
def home():
    number=100
    return render_template('index.html',value = number)

@app.route('/products')
def products():
   products_data=view_table('products')
   return render_template('products.html',products_data=products_data)


@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method=='POST':
        product_name=request.form['product_name']
        buying_price=request.form['buying_price']
        selling_price=request.form['selling_price']
        new_product=(product_name,buying_price,selling_price)
        insert_products(new_product)
        flash('product added successfully','success')
    return redirect(url_for('products'))


@app.route('/sales')
def sales():
    sales_data=view_table('sales')
    products=view_table('products')
    return render_template('sales.html',sales_data=sales_data,products=products)


@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    if request.method=='POST':
        pid=request.form['product_id']
        quantity=int(request.form['quantity'])
        new_sale=(pid,quantity)
        remining_stock=int(check_remaining_stock(pid))

        if remining_stock<quantity:
            flash('Insufficient stock,add more','danger')
    insert_sales(new_sale)

    return redirect(url_for('sales'))




@app.route('/login')
def login():
    return render_template('login.html') 


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        full_name=request.form['full_name']
        email=request.form['email']
        phone_no=request.form['phone_no']
        password=request.form['password']

        existing_user=check_user_exists(email)
        if not existing_user:
            hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
            new_user= (full_name,email,phone_no,hashed_password)
            create_user(new_user)
            flash('user created successfully','success')
        else:
            flash('user already exists,login instead','danger')



    return render_template('register.html')



@app.route('/stock')
def stock():
    stock_data=view_table('stock')
    products=view_table('products')
    return render_template('stock.html',stock_data=stock_data,products=products)




@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method=='POST':
        product_id=request.form['product_id']
        quantity=request.form ['stock_quantity']
        values=(product_id,quantity)
        insert_stock(values)
        flash('Stock Added Successfuly')

    return redirect(url_for('stock'))



@app.route('/index')
def index():
    return render_template('index.html')

app.run(debug=True)