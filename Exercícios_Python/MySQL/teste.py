import mysql.connector



try:
    print("conectando")
    mydb = mysql.connector.connect(
      host="localhost",
      user="root2",
      password="senha",
      database="bancodeteste" # Optional: specify a database
    )
    
    print(mydb)
    # Create a cursor object
    #mycursor = mydb.cursor()
    if mydb.is_connected():
        print("conectou")
    else:
        print("falhou")
    


# Execute an SQL query (e.g., creating a table)
    #mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Note: for data manipulation queries (INSERT, UPDATE, DELETE), you need to commit changes
    mydb.commit() 
    mydb.close()

    print("Table 'customers' created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    mydb.close()