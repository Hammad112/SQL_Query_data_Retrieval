import sqlite3

# Connect to sqlite
connection=sqlite3.connect('Student.db')

# cursor object to insert records,table creation,retrieve
cursor=connection.cursor()

# create table
table_info="""
CREATE TABLE Student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
First_Name TEXT NOT NULL,
Last_Name TEXT NOT NULL,
Degree_Name TEXT NOT NULL,
Section_Name TEXT NOT NULL,
Age INTEGER NOT NULL,
Marks REAL NOT NULL
)"""

## Creating Table
cursor.execute(table_info)

## inserting Records
cursor.execute('''INSERT INTO Student VALUES (1,'Hammad', 'Nasir', 'Computer Systems Engineering', 'A', 22, 96)''')
cursor.execute('''INSERT INTO Student VALUES (2,'Sarah', 'Johnson', 'Electrical Engineering', 'B', 24, 87)''')
cursor.execute('''INSERT INTO Student VALUES (3,'Michael', 'Smith', 'Mechanical Engineering', 'C', 21, 73)''')
cursor.execute('''INSERT INTO Student VALUES (4,'Emily', 'Davis', 'Civil Engineering', 'A', 23, 91)''')
cursor.execute('''INSERT INTO Student VALUES (5,'James', 'Brown', 'Biology', 'B', 25, 85)''')
cursor.execute('''INSERT INTO Student VALUES (6,'Olivia', 'Garcia', 'Computer Science', 'A', 19, 93)''')
cursor.execute('''INSERT INTO Student VALUES(7,'William', 'Martinez', 'Electrical Engineering', 'D', 20, 60)''')
cursor.execute('''INSERT INTO Student VALUES (8,'Sophia', 'Rodriguez', 'Mechanical Engineering', 'C', 22, 70)''')
cursor.execute('''INSERT INTO Student VALUES (9,'Benjamin', 'Wilson', 'Civil Engineering', 'B', 26, 88)''')
cursor.execute('''INSERT INTO Student VALUES (10,'Ava', 'Anderson', 'Biology', 'A', 21, 95)''')
cursor.execute('''INSERT INTO Student VALUES (11,'Isabella', 'Taylor', 'Computer Science', 'B', 23, 83)''')
cursor.execute('''INSERT INTO Student VALUES (12,'Liam', 'Thomas', 'Electrical Engineering', 'C', 20, 76)''')
cursor.execute('''INSERT INTO Student VALUES (13,'Mia', 'Moore', 'Mechanical Engineering', 'A', 22, 94)''')
cursor.execute('''INSERT INTO Student VALUES (14,'Alexander', 'White', 'Civil Engineering', 'B', 24, 82)''')
cursor.execute('''INSERT INTO Student VALUES (15,'Charlotte', 'Harris', 'Biology', 'C', 21, 74)''')
cursor.execute('''INSERT INTO Student VALUES (16,'Lucas', 'Clark', 'Computer Science', 'A', 23, 90)''')
cursor.execute('''INSERT INTO Student VALUES (17,'Amelia', 'Lewis', 'Electrical Engineering', 'D', 22, 63)''')
cursor.execute('''INSERT INTO Student VALUES (18,'Ethan', 'Walker', 'Mechanical Engineering', 'B', 24, 81)''')
cursor.execute('''INSERT INTO Student VALUES (19,'Harper', 'Hall', 'Civil Engineering', 'C', 25, 75)''')
cursor.execute('''INSERT INTO Student  VALUES (20,'Mason', 'Allen', 'Biology', 'A', 19, 97)''')

## Display All Records
print("Following are the inserted Records ->")

data=cursor.execute('''Select * From Student''')

for row in data:
    print(row)

## Closing Connection
connection.commit()
connection.close()

