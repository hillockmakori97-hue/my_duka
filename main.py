from flask import Flask,render_template,request,redirect,url_for
from database import view_table,insert_products,insert_sales,insert_stock,check_remaining_stock



app= Flask(__name__)
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
        print('product added successfully')
    return redirect(url_for('products'))


@app.route('/sales')
def sales():
    sales_data=view_table('sales')
    products=view_table('products')
    return render_template('sales.html',sales_data=sales_data,products=products)


@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    pid=request.form['product_id']
    quantity=request.form['quantity']
    new_sale=(pid,quantity)

    
    remining_stock=check_remaining_stock(pid)

    if remining_stock <quantity:
        print('Insufficient stock,add more')
    insert_sales(new_sale)
    
    return redirect(url_for('sales'))




@app.route('/login')
def login():
    return render_template('login.html') 


@app.route('/register')
def register():
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
        print('Stock Added Successfuly')
    return redirect(url_for('stock'))



@app.route('/index')
def index():
    return render_template('index.html')






app.run(debug=True)