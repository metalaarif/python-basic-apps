import pymysql

class PythonDB:
    '''Class for DB Connection'''
    connection = None   # to establish the connection
    cursor = None       # to run the commands

    def __init__(self):
        try:
            PythonDB.connection = pymysql.connect("127.0.0.1", "root", "", "pythondb")
            PythonDB.cursor = PythonDB.connection.cursor()
        except Exception as e:
            print(e.args)
        else:
            print("Connection Established Successfully")

    def createTable(self, tablename):
        try:
            command = '''CREATE TABLE %s (id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(50))''' %(tablename)
            PythonDB.cursor.execute(command)
        except Exception as e:
            print(e.args)
            print(command)
        else:
            print("Table created successfully")

    def addData(self, tablename, data):
        try:
            command = '''INSERT INTO %s (name) VALUES'''%(tablename)
            for name in data:
                command += "('"+name +"'),"
            #print(command)
            command = command.rstrip(",")
            #print(command)
            #PythonDB.cursor.execute(command)
        except Exception as e:
            print(e.args)
            print(command)
        else:
            PythonDB.connection.commit()
            print("%d records inserted successfully" %(len(data)))

    def listData(self, tablename):
        try:
            command = '''SELECT * FROM %s''' %(tablename)
            PythonDB.cursor.execute(command)
        except Exception as e:
            print(e.args)
            print(command)
        else:
            data = PythonDB.cursor.fetchall()
            for row in data:
                print(row)
    # def deletData(self, tablename, name):
    #     try:
    #         command = '''DELETE FROM %s WHERE name = '%s' '''%(tablename, name)
    #         PythonDB.cursor.execute(command)
    #     except Exception as e:
    #         print(e.args)
    #         print(command)
    #     else:
    #         PythonDB.connection.commit()
    #         print("Record deleted Successfully")

    def deletData(self, tablename, name):
        try:
            command = '''DELETE FROM %s WHERE name = '%s' '''%(tablename, name)
            command1 = '''DELETE FROM %s WHERE id = x ''' %(tablename)
            PythonDB.cursor.execute(command)
            PythonDB.cursor.execute(command1)
        except Exception as e:
            print(e.args)
            print(command)
            print(command1)
            PythonDB.connection.rollback()
        else:
            PythonDB.connection.commit()
            print("Record deleted Successfully")

p1 = PythonDB()
#p1.createTable("student")
#p1.addData("student", ['aarif', 'dragon', 'metal'])
p1.listData("student")
print("*" * 100)
p1.deletData("student", "aarif")
p1.listData("student")