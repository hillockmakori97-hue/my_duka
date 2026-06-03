import psycopg2
connection=psycopg2.connect(host='localhost',port=5432,user='postgres',password='rs3040bt',dbname='myduka')
waiter=connection.cursor()
waiter.execute('select * from products ')
print(waiter.fetchall())

