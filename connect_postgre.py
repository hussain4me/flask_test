import psycopg2


hostname = "localhost"
database = "demo"
username = "postgres"
pwd = "admin"
port_id = 5432


conn =None
cur =None
try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user = username,
        password = pwd,
        port = port_id)
    
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS employee")
    create_script =''' CREATE TABLE employee (
        id INT PRIMARY KEY,
        name varchar(40) NOT NULL,
        salary decimal(15,4),
        dept_id varchar(30)) '''    
    
    cur.execute(create_script)
    
    insert_script ="Insert into employee (id,name,salary,dept_id) VALUES(%s, %s, %s,%s)"
    insert_value =[(1, 'Zubair Hussain', 200000, 'D1'),(2, 'Zubair Naimat', 200000, 'D1'),(3, 'Oyewole Muiz', 200000, 'D1'),(4, 'Salami Ibrahim', 200000, 'D1')]
    for qry_value in insert_value:
        cur.execute(insert_script,qry_value)
        
        
    cur.execute('update employee set salary = salary + (salary * 0.5)')    
    cur.execute('delete from employee where id=4')    
    cur.execute('Select * from employee')
    
    for record in cur.fetchall():
        print(record[1], record[2])
    
    conn.commit()

except Exception as error:
    print(error)
    
    
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()