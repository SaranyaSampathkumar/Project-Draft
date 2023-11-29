import pathlib
import sqlite3
import pandas as pd

#path = None # use pathlib to get current working directory
path = pathlib.Path().cwd()

def create_db(db_name, filename, table_name):
    # create a path to the data file
    file_path = path / filename
      
    con = sqlite3.connect(db_name)# create a connection to the database
    cur = con.cursor() # create a cursor
      
    students = pd.read_csv(file_path) #students = None # read in the data 
    students.to_sql(table_name, con, index = False, if_exists = 'replace')     # insert the data into the specified table 
     
    # execute a select statement as f-string and print results to verify insertion
    results = cur.execute(f"SELECT * FROM {table_name}").fetchall()
    print(results)
    # commit the changes to the database
    con.commit()
    # close the connection
    con.close()


if __name__=="__main__":
    db_name = "School1.db"
    filename = "students_1.csv"
    table_name = "students"
    create_db(db_name, filename, table_name)
