import pymysql.cursors

class DbHelper():
    def __init__(self, host, id, pw, db, cursor_class):
        # self.connStr = 'host='s.snu.ac.kr',
        #     user='A4',
        #     password='4444',
        #     db='A4',
        #     charset='utf8',
        #     cursorclass=pymysql.cursors.DictCursor'
        self.connStr = "host='{0}',user = '{1}',password = '{2}',db = '{3}',charset = 'utf8',cursorclass = {4}".format(host,id,pw,db,cursor_class)
        self.conn


    # DB 연결하기
    def connectDB(self):
        self.conn = pymysql.connect(self.connStr)


    def selectTable(self , table):
        pass

    def deleteRow(self , table , key , value):
        pass

    def updateRow(self , table , key , value):
        pass

if __name__ == '__main__':
    pass