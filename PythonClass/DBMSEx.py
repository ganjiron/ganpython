import MySQLdb


class MyDB:
    def __init__(self):
        self.db = MySQLdb.connect('localhost', 'root', '4444', 'python_testdb')
        self.cursor = self.db.cursor()

    def testPrint(self):
        self.cursor.execute('select version()')
        data = self.cursor.fetchall()
        print(data)
        self.db.close()

    def createTable(self):
        self.cursor.execute("create table breakfast (\
                       name VARCHAR(32) PRIMARY KEY,\
                       spam INTEGER,\
                       eggs INTEGER,\
                       sausage INTEGER,\
                       prise FLOAT);")

    def fatchTest(self):
        min_price = 5


if __name__ == '__main__':
    my = MyDB()
    my.createTable()
