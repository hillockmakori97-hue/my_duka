import psycopg2
#enstablishing a connection to a postgres database 
conn=psycopg2.connect(host='localhost',port=5432,user='postgres',password='rs3040bt',dbname='my_duka')
curr=conn.cursor()
curr.execute('select * from products')
products_data=curr.fetchall()
print(products_data)