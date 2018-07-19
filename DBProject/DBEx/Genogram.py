import pymysql.cursors
class genoGram():
    def __init__(self):
        self.conn = pymysql.connect(
            host='s.snu.ac.kr',
            user='A4',
            password='4444',
            db='A4',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )

    def selectTab(self , argv):
        curs = self.conn.cursor()

        # SQL문 실행
        sql = "select * from {0}".format(argv)
        curs.execute(sql)

        # 데이타 Fetch
        rows = curs.fetchall()
        print(*rows,sep='\n')

        curs.close()



    # 아빠를 찾아라
    def findFather(self , id):
        curs = self.conn.cursor()
        sql = "select * from person\
        where id = (\
        select b.parent from person a , parentship b , marriage c\
        where a.id =  b.child\
        and b.parent = c.husband\
        and a.id = '{0}')".format(id)
        curs.execute(sql)
        rows = curs.fetchall()
        curs.close()
        return rows

    # 형제를 찾아라

    # 자식을 찾아라
    def findChild(self , id):
        curs = self.conn.cursor()
        sql = "select * from person \
        where id in ( \
        select b.child from person a , parentship b \
        where a.id =  b.parent \
        and a.id = '{0}')".format(id)
        curs.execute(sql)
        rows = curs.fetchall()
        curs.close()
        return rows

    # 사촌을 찾아라
    def find_cousins(self , id):

        fatherID = gg.findFather(id)
        print('아빠')
        print(fatherID[0]['id'])
        # 할아버지를 찾아라
        print('할배')
        grFaID = gg.findFather(fatherID[0]['id'])
        print(grFaID)

        # 아빠의 형제를 찾아라
        faBro = gg.findChild(grFaID[0]['id'])
        print('아빠형제')
        print(faBro)

        # 형제의 자식들을 찾아라
        cousin = []
        for i in range(len(faBro)):
            tmpCou = gg.findChild(faBro[i]['id'])
            cousin.append(tmpCou)
        print('사촌')
        # cousin.sort()
        print(cousin)


if __name__ == '__main__':
    gg = genoGram()
    # 아빠를 찾아라
    print("ID : ", end=' ')
    id = input()
    gg.find_cousins(id)




