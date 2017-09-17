import cx_Oracle

# default values
USER = "infa"
PASSWORD = "pass"
CONNECT_STRING = "localhost"

connection = cx_Oracle.connect(USER, PASSWORD, CONNECT_STRING)

cursor = connection.cursor()
cursor.execute("""
	    SELECT customer_id, cust_first_name, cust_last_name
	    FROM demo_customers
	    WHERE customer_id >:cid
""", cid=3)

for cid, cfname, clname in cursor:
    print("Values:", cid, cfname, clname)
