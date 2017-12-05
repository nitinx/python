from nxcommon import NXOracle
'''
# Open KEY files
with open('c:\\DEV\\GitHub\\python\\3.x\\keys\\oracle.key') as key_file_oracle:
    key_oracle = json.load(key_file_oracle)

connection = cx_Oracle.connect(key_oracle[0]['USER'],
                               key_oracle[0]['PASSWORD'],
                               key_oracle[0]['CONNECT_STRING'])
'''

connection = NXOracle().db_login()
cursor = connection.cursor()

cursor.execute("""
	    SELECT customer_id, cust_first_name, cust_last_name
	    FROM demo_customers
	    WHERE customer_id >:cid
""", cid=3)

for cid, cfname, clname in cursor:
    print("Values:", cid, cfname, clname)
