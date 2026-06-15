import psycopg2
#enstablishing a connection to a postgres database 
conn=psycopg2.connect(host='localhost',port=5432,user='postgres',password='rs3040bt',dbname='my_duka')
curr=conn.cursor()
products_data=[]
def view_products(products_data):
    curr.execute('select * from products' )
    products_data=curr.fetchall()
    return products_data
print(view_products(products_data))
curr.execute("insert into products(name,buying_price,selling_price) values('shirt',1500,2000)")
conn.commit()
print(products_data)


def insert_products(values):
    curr.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()
# product1=('comb',50,70)
# insert_products(product1)
# print(products_data)


def insert_products2 (values):
    curr.execute('insert into products (name,buying_price,selling_price) values(%s,%s,%s)',values)
    conn.commit()
products3=('CPU',4500,5000)
insert_products2(products3)
print(products3)


def insert_sales(values):
    curr.execute('insert into sales (pid,quantity) values(%s,%s)',values)
    conn.commit()
sales1=(3,3)


def view_table(table_name):
    curr.execute(f"select * from {table_name}")
    records=curr.fetchall()
    return records


# insert_sales(sales1)
print(view_table("sales"))
sale2=(4,5)
sale3=(6,11)
insert_sales(sale2)
insert_sales(sale3)
sales_records=view_table("sales")
print(sales_records)

def insert_stock(values):
    curr.execute("insert into stock(pid,stock_quantity) values(%s,%s)",values)
    conn.commit()
stock1=(1,100)
stock2=(2,100)
stock3=(3,80)
insert_stock(stock1)
insert_stock(stock2)
insert_stock(stock3)
print(view_table("stock"))
def sales_per_day():
    curr.execute("""
      select date(sales.created_at) as date, sum(sales.quantity * products.selling_price) as
      total_sales from sales join products on products.id = sales.pid  group by date;
    """)
    daily_sales = curr.fetchall()
    return daily_sales


def sales_per_day():
    curr.execute("""
      select date(sales.created_at) as date, sum(sales.quantity * products.selling_price) as
      total_sales from sales join products on products.id = sales.pid  group by date;
    """)
    daily_sales = curr.fetchall()
    return daily_sales


def profit_per_day():
    curr.execute("""
        select date(sales.created_at) as date, sum(sales.quantity *( products.selling_price -
        products.buying_price)) as total_sales from sales join products on products.id = sales.pid
         group by date;
    
    """)
    daily_profit = curr.fetchall()
    return daily_profit



def sales_per_product():
    curr.execute("""
        select products.name as p_name , sum(sales.quantity * products.selling_price)  as total_sales
        from products join sales on sales.pid = products.id group by p_name;
    """)
    product_sales = curr.fetchall()
    return product_sales


def profit_per_product():
    curr.execute("""
        select products.name as p_name , sum(sales.quantity *( products.selling_price - 
        products.buying_price))  as total_sales from products join sales on sales.pid = products.id group by p_name;
    """)
    product_profit = curr.fetchall()
    return product_profit

def check_remaining_stock(pid):
    curr.execute('select sum(stock.stock_quantity) from stock where pid=%s' (pid,))
    total_stock=curr.fetchone()[0] or 0 
    curr.execute('select sum(sales.quantity) from sales where pid=%s',(pid,))
    total_sold=curr.fetchone()[0] or 0 
    return total_stock - total_sold
# class horse 2
#iden