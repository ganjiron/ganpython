import pymysql.cursors
conn = pymysql.connect(
            host='s.snu.ac.kr',
            user='A4',
            password='suck0070',
            db='A4',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
try:
    with conn.cursor() as cursor:
        sql = 'select * from class'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    conn.close()