import pymysql.cursors
class dbProv():
    def __init__(self):
        self.conn = pymysql.connect(
            host='s.snu.ac.kr',
            user='A4',
            password='4444',
            db='A4',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )

    def con(self):
        connection = pymysql.connect(
            host='s.snu.ac.kr',
            user='A4',
            password='4444',
            db='A4',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )

    # 모든 학생의 이름과 주민등록번호
    def selectNameofStdudent(self):
        curs = self.conn.cursor()

        # SQL문 실행
        sql = "select name , resident_id from student"
        curs.execute(sql)

        # 데이타 Fetch
        rows = curs.fetchall()
        # print(rows)  # 전체 rows
        # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
        # print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')
        # for i in rows:
        #     print(i)
        print(*rows,sep='\n')

        curs.close()


    # 최성희 교ㅕ수보다 늦게 임용한 교수들의 이름!재직년수!
    def selectNameOfProfessor(self):
        curs = self.conn.cursor()

        # SQL문 실행
        sql1 = "select name , resident_id from student"
        sql = 'select name , year(now()) - year_emp from professor where year_emp > (select year_emp from professor where name = "최성희")'
        curs.execute(sql)

        # 데이타 Fetch
        rows = curs.fetchall()
        # print(rows)  # 전체 rows
        # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
        # print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')
        # for i in rows:
        #     print(i)
        print(*rows,sep='\n')
        curs.close()


    def selectGrade(self , argv):
        curs = self.conn.cursor()

        # SQL문 실행
        sql = "select c.title , b.grade from student a , takes b , course c , class d\
        where a.stu_id = b.stu_id\
        and b.class_id = d.class_id\
        and d.course_id = c.course_id\
        and a.name = '{0}' ".format(argv)
        curs.execute(sql)

        # 데이타 Fetch
        rows = curs.fetchall()
        # print(*rows, sep='\n')
        print("이름 : " , argv)
        print("과목명\t성적")
        for i in rows:
            print("{0}\t{1}".format(i['title'] , i['grade']))
        curs.close()

    def deleteTest(self , argv):
        curs = self.conn.cursor()
        sql = 'delete from takes where stu_id = {0}'.format(argv)
        curs.execute(sql)
        self.conn.commit()

if __name__ == '__main__':
    try:
        a = dbProv()
        # a.selectNameofStdudent()
        # a.selectNameOfProfessor()
        # a.selectGrade(input())
        print("지울사람ID : " , end=' ' )
        a.deleteTest( input())
    except Exception as ex:
        print(ex)
    finally:
        a.conn.close()