import psycopg2
connection=psycopg2.connect(host='localhost',port=5432,user='postgres',password='rs3040bt',dbname='my_duka')
waiter=connection.cursor()
waiter.execute('select * from sales')
result=waiter.fetchall()
print(result)