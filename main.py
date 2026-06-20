from flask import Flask,render_template,request,redirect,url_for,flash,session
from database import view_table,insert_products,insert_sales,insert_stock,check_remaining_stock,check_user_exists,create_user,sales_per_day,sales_per_product,profit_per_product,profit_per_day
from flask_bcrypt import Bcrypt
import os
from functools import wraps
app= Flask(__name__)
# bcrypt instance with flask app
bcrypt=Bcrypt(app)

app.secret_key=os.urandom(24)
@app.route('/')
def home():
    number=100
    return render_template('index.html',value = number)

def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected


@app.route('/products')
@login_required
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
@login_required
def sales():
    sales_data=view_table('sales')
    products=view_table('products')
    return render_template('sales.html',sales_data=sales_data,products=products)


@app.route('/add_sales',methods=['GET','POST'])
@login_required
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




@app.route('/login',methods=('GET','POST'))
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        registered_user=check_user_exists(email)
        if not registered_user:
            flash('Non Existent user, please register','danger')
        else:
            if bcrypt.check_password_hash(registered_user[-1],password):
                session['email']=email
                flash('login succes','success')
                return redirect(url_for('dashboard'))
            else:
                flash('incorrect password,try again','danger')
            # return
        
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
@login_required
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

@app.route('/dashboard')
def dashboard():
    product_sales=sales_per_product()
    product_profit=profit_per_product()

    daily_sales=sales_per_day()
    daily_profit=profit_per_day()

    product_names= [i[0] for i in product_sales]
    prod_profit= [ float(i[1]) for i in product_profit]
    prod_sales=[float(i[1]) for i in product_sales]


    dates=[str(i[0]) for i in daily_sales]
    day_sales=[float(i[1]) for i in daily_sales]
    day_profit=[float(i[1]) for i in daily_profit]


    return render_template('dashboard.html',
                        product_names=product_names,prod_profit=prod_profit,prod_sales=prod_sales,
                        dates=dates,day_sales=day_sales,day_profit=day_profit)

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/logout')
def logout():
    session.pop('email',None)
    flash('Logged out successfully','success')
    return redirect(url_for('login'))
app.run(debug=True)